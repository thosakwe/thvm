.globl main
.data
    msg: .asciiz "Hello, thvm!\n"
.text
    main:
        set $r0, msg # Load the address of the string
        int 4 # Syscall
