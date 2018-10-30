import std.file;
import std.stdio;
import text.lexer;

int main(string[] args)
{
	if (args.length < 2) {
		writeln("usage: thasm [options...] <input_file>");
		return 1;
	}

	immutable inputFile = args[1];
	auto lexer = new Lexer(inputFile);
	lexer.scan(std.file.readText(inputFile));

	return 0;
}
