THVM Specification

Table of Contents

1. Overview
2. Machine
    2.1. CPU
      2.1.1. Registers
      2.1.2. Scheduler
    2.2. MMU
    2.3. Timer
3. Executable Format
4. Instructions
5. Opcodes

1. Overview

Tobe Henry's Virtual Machine, abbreviated as THVM, is an educational project
aimed at constructing a 16-bit virtual machine.

2. Machine

THVM, like any other computer machine, consists of several components:
    * The central processing unit (CPU)
    * The memory management unit (MMU)
    * The timer

2.1. CPU

2.1.1. Registers

THVM's CPU has 16 16-bit general-purpose registers, named $r0, $r1, ..., $r15.
In addition to these registers, the CPU has an 8-bit $flag register.

2.1.2. Scheduler

The CPU supports multiple threads of execution, in a cooperative multi-tasking style.
The program starts in a thread that is created by default. Threads may spawn other threads.
For a thread to suspend its current execution, it may place a return address into 
$r0, and yield. When the scheduler reaches the thread again, it will resume execution at
$r0. If $r0 is zero, the thread will be terminated.

2.2. MMU

THVM's memory management operates in terms of 4MiB pages.
Each page is divided into regions, each with a set of permissions dictating
how it may be accessed. A given region within a page may be any combination of the following:
    * readable
    * writable
    * executable
    * permissions-writable

The instructions of a page are loaded into a region that is only executable. Any constants/variables
defined in the executable are loaded into a region that is both readable and writable, but not executable
or permissions-writable.

Programs are permitted to change the permissions of a region, if, and only if that region is
permissions-writable. Once a region is marked as non-permissions-writable, its permissions cannot be changed again.

Programs can query:
* Which page execution is currently taking place in (returns a 16-bit id in $r0)
* The region execution is taking place in (returns a 16-bit id in $r0)
* The number of regions in the current page (returns a number in $r0)
* The start and end offset of a given region within a page (start in $r0, end in $r1)

2.3. Timer

THVM has a simple timer, which has two states: "ON" and "OFF". While the timer
is "ON", every millisecond, a 16-bit counter is incremented. When the state becomes
"OFF", the value of this counter is stored somewhere (a register), and then is set to zero.

The timer's value may be set to a known value, while it is in the "OFF" state. This effectively
lets a thread logically "resume" a previous count.

3. Executable Format

4. Instructions

Instructions for THVM are 2 bytes long:

15         8        0
+---------+---------+
|   arg   | opcode  |
+---------+---------+

5. Opcodes
