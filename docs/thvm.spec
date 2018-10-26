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

THVM runs a single startup program upon boot. The format of this program must be the following:
    * 8-bit version
    * 8-bit flags
    * 16-bit checksum
        * byte 0 = 0xBAADBEEF
        * byte 1 = (version + (flags / 2))
    * 64-bits: length <data_len> of .data section
    * <data_len> bytes: .data section
    * 64-bits: length <text_len> of .text section
    * <text_len> bytes: .text section

    <data_len> and <text_len> must be even numbers.

4. Instructions

Instructions for THVM are 2 bytes long:

15         8        0
+---------+---------+
|   arg   | opcode  |
+---------+---------+

Some instructions require 16-bit arguments; however, instructions are 16 bits in total.
In these cases, the arg byte is an encoding of the actual argument, according to this algorithm:
    * Let x be the actual 16-bit argument, ex. an immediate value.
    * Let y = x / 256.
    * The value of the arg byte will be y.

5. Opcodes

Mnemonics:
    * <reg> - The 8-bit index of a register. ex. 0 for $r0, 4 for $r4.
    * <imm8> - An 8-bit value.
    * <imm16> - A 16-bit value, divided by 256. (Ultimately an 8-bit value).

ADD <reg> - Adds the value of <reg> into $r0.
ADDI <imm16> - Adds an immediate value into $r0.
MOV <reg> - Moves 
