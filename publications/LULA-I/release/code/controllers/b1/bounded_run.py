"""Windows job-object resource controls for one isolated benchmark/build job.

Launch suspended, impose inherited affinity, BelowNormal priority and a 2.75 GiB
per-process committed-memory limit, then resume. Only this job tree is terminated.
No shell is involved; command arguments are passed as an argv list.
"""
import argparse
import ctypes as C
from ctypes import wintypes as W
import json
import os
from pathlib import Path
import subprocess
import time

K = C.WinDLL('kernel32', use_last_error=True)
N = C.WinDLL('ntdll')
SIZE = C.c_size_t

class Basic(C.Structure):
    _fields_ = [('PerProcessUserTimeLimit', C.c_int64), ('PerJobUserTimeLimit', C.c_int64),
                ('LimitFlags', W.DWORD), ('MinimumWorkingSetSize', SIZE),
                ('MaximumWorkingSetSize', SIZE), ('ActiveProcessLimit', W.DWORD),
                ('Affinity', SIZE), ('PriorityClass', W.DWORD), ('SchedulingClass', W.DWORD)]

class IO(C.Structure):
    _fields_ = [(n, C.c_uint64) for n in ('ReadOperationCount', 'WriteOperationCount',
                 'OtherOperationCount', 'ReadTransferCount', 'WriteTransferCount', 'OtherTransferCount')]

class Extended(C.Structure):
    _fields_ = [('BasicLimitInformation', Basic), ('IoInfo', IO),
                ('ProcessMemoryLimit', SIZE), ('JobMemoryLimit', SIZE),
                ('PeakProcessMemoryUsed', SIZE), ('PeakJobMemoryUsed', SIZE)]

class Memory(C.Structure):
    _fields_ = [('cb', W.DWORD), ('PageFaultCount', W.DWORD)] + [(n, SIZE) for n in
               ('PeakWorkingSetSize', 'WorkingSetSize', 'QuotaPeakPagedPoolUsage',
                'QuotaPagedPoolUsage', 'QuotaPeakNonPagedPoolUsage', 'QuotaNonPagedPoolUsage',
                'PagefileUsage', 'PeakPagefileUsage', 'PrivateUsage')]

K.CreateJobObjectW.argtypes = [C.c_void_p, W.LPCWSTR]
K.CreateJobObjectW.restype = W.HANDLE
K.SetInformationJobObject.argtypes = [W.HANDLE, C.c_int, C.c_void_p, W.DWORD]
K.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
K.TerminateJobObject.argtypes = [W.HANDLE, W.UINT]
K.CloseHandle.argtypes = [W.HANDLE]
K.K32GetProcessMemoryInfo.argtypes = [W.HANDLE, C.c_void_p, W.DWORD]
N.NtResumeProcess.argtypes = [W.HANDLE]
N.NtResumeProcess.restype = C.c_long

def checked(ok):
    if not ok:
        raise C.WinError(C.get_last_error())

def topology():
    size = W.DWORD()
    K.GetLogicalProcessorInformationEx(0, None, C.byref(size))
    buf = C.create_string_buffer(size.value)
    checked(K.GetLogicalProcessorInformationEx(0, buf, C.byref(size)))
    data = buf.raw
    rows = []
    off = 0
    while off < size.value:
        relationship = int.from_bytes(data[off:off+4], 'little')
        length = int.from_bytes(data[off+4:off+8], 'little')
        if not length:
            raise RuntimeError('Invalid processor topology record')
        if relationship == 0:
            groups = int.from_bytes(data[off+30:off+32], 'little')
            for g in range(groups):
                mask = int.from_bytes(data[off+32+16*g:off+40+16*g], 'little')
                group = int.from_bytes(data[off+40+16*g:off+42+16*g], 'little')
                rows.append({'physical_core': len(rows), 'group': group,
                             'logical_processors': [i for i in range(64) if mask & (1 << i)],
                             'mask': mask, 'smt': bool(data[off+8] & 1),
                             'efficiency_class': data[off+9]})
        off += length
    return rows

def run(argv, prefix, cwd, cpu=0, timeout=600, env=None):
    prefix = Path(prefix).resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    meta = {'argv': argv, 'cwd': str(Path(cwd).resolve()), 'logical_cpu': cpu,
            'affinity_mask': 1 << cpu, 'priority': 'BelowNormal', 'memory_limit_bytes': 2952790016,
            'timeout_seconds': timeout, 'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'status': 'starting', 'peak_working_set_bytes': 0, 'peak_private_bytes': 0}
    metafile = prefix.with_suffix('.process.json')
    job = K.CreateJobObjectW(None, None)
    checked(job)
    limits = Extended()
    # PROCESS_MEMORY | KILL_ON_JOB_CLOSE | AFFINITY | PRIORITY_CLASS
    limits.BasicLimitInformation.LimitFlags = 0x100 | 0x2000 | 0x10 | 0x20
    limits.BasicLimitInformation.Affinity = 1 << cpu
    limits.BasicLimitInformation.PriorityClass = 0x4000
    limits.ProcessMemoryLimit = meta['memory_limit_bytes']
    proc = None
    started = time.perf_counter()
    try:
        checked(K.SetInformationJobObject(job, 9, C.byref(limits), C.sizeof(limits)))
        with prefix.with_suffix('.stdout.txt').open('wb') as out, prefix.with_suffix('.stderr.txt').open('wb') as err:
            child_env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
                             MKL_NUM_THREADS='1', RAYON_NUM_THREADS='1', CARGO_BUILD_JOBS='1')
            child_env.update(env or {})
            proc = subprocess.Popen(argv, cwd=cwd, env=child_env, stdout=out, stderr=err,
                                    creationflags=0x4 | 0x4000 | 0x08000000)
            checked(K.AssignProcessToJobObject(job, int(proc._handle)))
            meta.update(pid=proc.pid, status='running')
            metafile.write_text(json.dumps(meta, indent=2), encoding='utf-8')
            if N.NtResumeProcess(int(proc._handle)) != 0:
                raise RuntimeError('NtResumeProcess failed')
            while proc.poll() is None:
                m = Memory()
                m.cb = C.sizeof(m)
                if K.K32GetProcessMemoryInfo(int(proc._handle), C.byref(m), C.sizeof(m)):
                    meta['peak_working_set_bytes'] = max(meta['peak_working_set_bytes'], m.PeakWorkingSetSize)
                    meta['peak_private_bytes'] = max(meta['peak_private_bytes'], m.PrivateUsage)
                if time.perf_counter() - started > timeout:
                    checked(K.TerminateJobObject(job, 124))
                    meta['status'] = 'timeout'
                    break
                time.sleep(0.1)
            meta['exit_code'] = proc.wait()
            # The retained process handle exposes the kernel peak after exit;
            # polling alone can miss a short process's entire active interval.
            m = Memory()
            m.cb = C.sizeof(m)
            if K.K32GetProcessMemoryInfo(int(proc._handle), C.byref(m), C.sizeof(m)):
                meta['peak_working_set_bytes'] = max(meta['peak_working_set_bytes'], m.PeakWorkingSetSize)
                meta['peak_private_bytes'] = max(meta['peak_private_bytes'], m.PeakPagefileUsage)
            if meta['status'] != 'timeout':
                meta['status'] = 'completed' if meta['exit_code'] == 0 else 'failed'
    except BaseException:
        if proc is not None:
            K.TerminateJobObject(job, 125)
            proc.wait()
        meta['status'] = 'controller_error'
        raise
    finally:
        meta['wall_seconds'] = time.perf_counter() - started
        meta['end_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        metafile.write_text(json.dumps(meta, indent=2), encoding='utf-8')
        K.CloseHandle(job)
    return meta

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--cpu', type=int, default=0)
    ap.add_argument('--timeout', type=float, default=600)
    ap.add_argument('--prefix')
    ap.add_argument('--cwd', default=os.getcwd())
    ap.add_argument('--topology', action='store_true')
    ap.add_argument('command', nargs=argparse.REMAINDER)
    a = ap.parse_args()
    if a.topology:
        print(json.dumps(topology(), indent=2))
    else:
        cmd = a.command[1:] if a.command[:1] == ['--'] else a.command
        if not a.prefix or not cmd:
            ap.error('--prefix and command are required')
        result = run(cmd, a.prefix, a.cwd, a.cpu, a.timeout)
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if result['status'] == 'completed' else 1)
