# C Code Interpreter

Welcome to the C Code Interpreter! This project is a powerful and elegantly crafted interpreter for C code, built using Python and PLY (Python Lex-Yacc). Whether you're a student, developer, or recruter this interpreter provides a great way to dive deep into the world of C programming and compilers.

## Why You'll Love It

- **Lexical Analysis**: Harnessed PLY's lexer to break down C code into tokens with impressive efficiency.
- **Syntax Parsing**: The parser meticulously handles C grammar, ensuring your code is syntactically sound.
- **Semantic Analysis**: It performs rigorous semantic checks to make sure your code isn't just correct, but meaningful.
- **Clean Codebase**: Clean, well-documented codebase that's easy to understand and extend.
- **Error Handling**: The interpreter offers robust error detection and clear, helpful messages to make debugging a breeze.

## Getting Started

### Setup

First things first, let's get you set up:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/C-Language-Compiler-in-Python.git
    cd C-Language-Compiler-in-Python/Compilador
    ```

### Running the Interpreter

Ready to run some code? Use this command:
```sh
python interpreter.py <input_file>
```
Replace `<input_file>` with the path to your C code file.

### Example

Let's see it in action! Here's a sample C program:

```c
main{
	int a,b,x,y,i,j;	
	writeln("I can write!");
	a = 5;
	b =  a + 3;
	x = b +5;
	y = x + a;		
	j = j * 5;
	writeln("yo"*2);
	if ( ( a>b) and (a*5+(b+4)) ) 
	{
		i = a*5+(b+4);
		writeln("true");
		writeln(a);
	}else
	{
		if(y<x)
		{
			i = x * (b * y);
			writeln(x);
			writeln("if case");
		}else
		{
			writeln("else case");
		}
	}
	writeln(i);	
}
```

When you run this program through our interpreter, you'll get the following output:

```
I can write!
yoyo
else case
0
```

### How It Works

1. **Lexical Analysis**: The lexer scans the code and splits it into tokens.
2. **Syntax Parsing**: The parser then builds a syntax tree, mapping out the structure of your C code.
3. **Semantic Analysis**: The code checks that the code makes sense and follows C language rules.
4. **Interpretation**: Finally, the interpreter executes the code based on the parsed syntax and semantics.

### Behind the Scenes: Using Sets

To keep things organized and efficient, I used sets to pass the parser to the interpreter. This approach helps maintain context for variables, functions, and control structures, ensuring the interpreter faithfully follows the logic of the code.
