module text.token;
import text.span;

enum TokenType
{
    // Registers
    R0,
    R1,
    R2,
    R3,
    R4,
    R5,
    R6,
    R7,
    R8,
    R9,
    R10,
    R11,
    R12,
    R13,
    R14,
    R15,

    // Instructions
    ADD,
    DIV,
    MOV,
    MUL,
    SUB,
}

class Token
{
public:
    TokenType getType() const
    {
        return type;
    }

    const(Span) getSpan() const
    {
        return span;
    }

private:
    TokenType type;
    Span span;
}
