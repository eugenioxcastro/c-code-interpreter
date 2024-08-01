import ply.yacc as yacc
import ply.lex as lex
from myLexer import lexer
from myParser import parser
from myInterpreter import find_valid_tuples, run_statements, symbol_table

with open("program.txt", "r") as file:
    program = file.read()

result = parser.parse(program)
valid_tuples = find_valid_tuples(result)

# running my program instruction by instruction
run_statements(valid_tuples)
