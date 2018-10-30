module text.span;

import std.string;

/// Represents a location in text.
class Span
{
public:
    /// The line at which this span is found.
    int line;

    /// The column within the line.
    int column;

    /// The length of this span.
    int length;

    string filename;

    string sourceText;

    /// Returns the text of this span.
    string getText()
    {
        int start = 0;
        auto lines = splitLines(sourceText);

        for (int i = 0; i < line; i++)
        {
            start += lines[i].length;
        }

        start += column;

        return sourceText[start .. (start + length)];
    }
}
