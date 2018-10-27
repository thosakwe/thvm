parser grammar ThasmParser;

tokens {
    BRACKET_L, BRACKET_R, COMMA, COLON, DOLLAR, PAREN_L, PAREN_R,
    ASCIIZ, BYTE, DATA, GLOBAL, RESB, RESW, TEXT, WORD,
    DIV, MINUS, MOD, PLUS, SHL, SHR, TIMES,
    HEX, INT, NAME, STRING,

    // regs
    R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12,
    R13, R13, R14, R15,

    // insns
    ADD, NOP
}

asm: metadata* section*;

metadata:
    GLOBAL NAME #GlobalMetadata
;

section: dataSection | textSection;

dataSection: DATA dataStmt*;

dataStmt: NAME COLON dataValue (TIMES multipler=constant)?;

dataValue: 
    ASCIIZ STRING #DataString
    | BYTE constant #DataByte
    | WORD constant #DataWord
    | (RESB | RESW) constant #DataReserve
;

constant:
    INT #IntConstant
    | HEX #HexConstant
    | DOLLAR #DollarConstant
    | left=constant (TIMES|DIV|MOD) right=constant #TimesDivModConstant
    | left=constant (PLUS|MINUS) right=constant #PlusMinusConstant
    | left=constant (SHL|SHR) right=constant #ShlShrConstant
    | PAREN_L constant PAREN_R #ParenConstant
;

textSection: TEXT textStmt*;

textStmt: textLabel | textInstruction;

textLabel: NAME COLON;

textInstruction:
    ADD dst=reg COMMA src=reg #AddInsn
    | ADD constant #AddImmInsn
    | NOP #NopInsn
;

reg:
    R0 | R1 | R2 | R3 | R4 | R5 | R6 | R7  | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15;