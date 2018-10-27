lexer grammar ThasmLexer;

CMT: '#' (~'\n')* -> skip;
WS: [ \n\r\t]+ -> skip;

// Symbols
BRACKET_L: '[';
BRACKET_R: ']';
COLON: ':';
COMMA: ',';
DOLLAR: '$';
PAREN_L: '(';
PAREN_R: ')';

// Keywords
ASCIIZ: '.asciiz';
BYTE: '.byte';
DATA: '.data';
EQU: 'equ';
GLOBAL: '.globl';
RESB: 'resb';
RESW: 'resw';
TEXT: '.text';
WORD: '.word';

// Registers
R0: '$' [Rr] '0';
R1: '$' [Rr] '1';
R2: '$' [Rr] '2';
R3: '$' [Rr] '3';
R4: '$' [Rr] '4';
R5: '$' [Rr] '5';
R6: '$' [Rr] '6';
R7: '$' [Rr] '7';
R8: '$' [Rr] '8';
R9: '$' [Rr] '9';
R10: '$' [Rr] '10';
R11: '$' [Rr] '12';
R12: '$' [Rr] '12';
R13: '$' [Rr] '13';
R14: '$' [Rr] '14';
R15: '$' [Rr] '15';

// Instructions
ADD: [Aa][Dd][Dd];
NOP: [Nn][Oo][Pp];

// Operators
TIMES: '*';
DIV: '/';
MOD: '%';
PLUS: '+';
MINUS: '-';
SHL: '<<';
SHR: '>>';

// Values
NAME: [A-Za-z_][A-Za-z0-9_]*;