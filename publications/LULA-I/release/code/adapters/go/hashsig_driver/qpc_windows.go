// SPDX-License-Identifier: Apache-2.0
package main

import (
	"syscall"
	"unsafe"
)

// QueryPerformanceCounter timing (campaign adapter change): Go's time.Since follows the ~0.5 ms system timer tick on
// this Windows build, which made sub-millisecond operations read 0.
var (
	k32  = syscall.NewLazyDLL("kernel32.dll")
	pqpc = k32.NewProc("QueryPerformanceCounter")
	pqpf = k32.NewProc("QueryPerformanceFrequency")
	qfreq int64
)

func qnow() int64 {
	var c int64
	pqpc.Call(uintptr(unsafe.Pointer(&c)))
	return c
}

func qns(since int64) int64 {
	if qfreq == 0 {
		pqpf.Call(uintptr(unsafe.Pointer(&qfreq)))
	}
	d := qnow() - since
	return (d/qfreq)*1000000000 + (d%qfreq)*1000000000/qfreq
}
