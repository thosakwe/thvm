# thasm
`thasm` is the assembler for `thvm`. `thasm` compiles
Intel-syntax Assembly instructions into valid `thvm` binaries.

## Usage
```bash
thasm -o foo.bin foo.asm
```

## Example
```asm
.globl main
.data
    msg: .asciiz "Hello, thvm!\n"
.text
    main:
        set $r0, msg # Load the address of the string
        int 4 # Print
```

## Grammar
This is just a grammar that does no checking. The real
implementation is based on ANTLR, and enforces valid code semantics.

```ebnf
assembly ::= metadata* section*;

metadata ::= global;

global ::= ".globl" NAME;

section ::= data_section | text_section;

data_section ::= ".data" data_stmt*;

data_stmt ::= NAME ":" data_value data_multiplier?;

data_value ::= data_string | data_byte | data_word | data_reserve;

data_string ::= ".asciiz" STRING;

data_byte ::= ".byte" INT;

data_word ::= ".word" INT;

data_reserve ::= ("resb" | "resw") INT;

data_multiplier ::= "*" INT;

text_section ::= ".text" text_stmt;

text_stmt ::= label | instruction;

label ::= NAME ":";

instruction ::= NAME operands?;

operands: operand ("," operand)?;

operand: NAME | INT | dereference | offset;

dereference ::= "[" NAME "]";

offset ::= NAME ":" NAME;
```