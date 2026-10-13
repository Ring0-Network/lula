"""Low-cost 1 Hz sampler (replaces sampler.ps1, whose WMI queries cost 20-90 % of a core and contaminated the gate).
Uses NtQuerySystemInformation(SystemProcessorPerformanceInformation) and CallNtPowerInformation through ctypes: no WMI, no child processes.
Columns: utc,total_utility,cpu10_utility,cpu11_utility,cpu10_freq_mhz,busy_processes (always empty here).
Utility = 100 * (1 - idle delta / (kernel+user delta)) per logical processor, the standard definition on the system counters;
it can differ slightly from the Task Manager 'utility' figure, which also scales by frequency."""
import ctypes as C, datetime as dt, sys, time
from ctypes import wintypes as W
from pathlib import Path

from release_paths import CODE, RELEASE, campaign, results, build
S = campaign('b1', rerun=True)
RESULTS = results('b1')
BUILD = build()
(S / 'raw').mkdir(parents=True, exist_ok=True)
(S / 'vectors').mkdir(parents=True, exist_ok=True)
OUT, STOP = S / 'raw' / 'sampler.csv', S / 'raw' / 'sampler.stop'
nt = C.WinDLL('ntdll'); pw = C.WinDLL('powrprof'); k32 = C.WinDLL('kernel32')
k32.SetPriorityClass(k32.GetCurrentProcess(), 0x4000)      # BELOW_NORMAL_PRIORITY_CLASS
NCPU = C.c_uint32(0)
class SPPI(C.Structure):
    _fields_ = [('IdleTime', C.c_int64), ('KernelTime', C.c_int64), ('UserTime', C.c_int64), ('DpcTime', C.c_int64),
                ('InterruptTime', C.c_int64), ('InterruptCount', C.c_uint32)]
class PPI(C.Structure):
    _fields_ = [('Number', C.c_uint32), ('MaxMhz', C.c_uint32), ('CurrentMhz', C.c_uint32), ('MhzLimit', C.c_uint32),
                ('MaxIdleState', C.c_uint32), ('CurrentIdleState', C.c_uint32)]
info = C.create_string_buffer(8)
n = k32.GetActiveProcessorCount(0xFFFF) or 14
arr = (SPPI * n)()
parr = (PPI * n)()

def read():
    ret = C.c_ulong(0)
    nt.NtQuerySystemInformation(8, C.byref(arr), C.sizeof(arr), C.byref(ret))
    return [(a.IdleTime, a.KernelTime + a.UserTime) for a in arr]

def freq(i):
    pw.CallNtPowerInformation(11, None, 0, C.byref(parr), C.sizeof(parr))
    return parr[i].CurrentMhz

if not OUT.exists():
    OUT.write_text('utc,total_utility,cpu10_utility,cpu11_utility,cpu10_freq_mhz,busy_processes\n', encoding='ascii')
prev = read()
with open(OUT, 'a', encoding='ascii') as f:
    while not STOP.exists():
        time.sleep(1.0)
        cur = read()
        u = []
        for (i0, b0), (i1, b1) in zip(prev, cur):
            d = b1 - b0
            u.append(100.0 * (1.0 - (i1 - i0) / d) if d > 0 else 0.0)
        tot_idle = sum(c[0] - p[0] for c, p in zip(cur, prev)); tot_all = sum(c[1] - p[1] for c, p in zip(cur, prev))
        total = 100.0 * (1.0 - tot_idle / tot_all) if tot_all > 0 else 0.0
        f.write(f"{dt.datetime.now(dt.timezone.utc).isoformat()},{total:.1f},{u[10]:.1f},{u[11]:.1f},{freq(10)},\n")
        f.flush()
        prev = cur
