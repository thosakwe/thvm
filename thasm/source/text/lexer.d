module text.lexer;

import text.span;
import text.token;

class Lexer
{
public:
    this(string filename)
    {
        this.filename = filename;
    }

    const(Token[]) getTokens() const
    {
        return tokens;
    }

    void scan(string text)
    {

    }

private:
    string filename;
    Token[] tokens;
}
