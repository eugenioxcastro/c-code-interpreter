import ply.lex as lex

reserved = {
    'program': 'PROGRAM',
    'main': 'MAIN',
    'int': 'INT',
    'double': 'DOUBLE',
    'float': 'FLOAT',
    'string': 'STRING',
    'bool': 'BOOL',
    'char': 'CHAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'write': 'WRITE',
    'writeln': 'WRITELN',
    'void': 'VOID',
}

tokens = [
    'NUMBER',
    'EQUAL',
    'INCREMENT',
    'DECREMENT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'LPAREN',
    'RPAREN',
    'ID',
    'RBRACE',
    'LBRACE',
    'SEMI',
    'COMMA',
    'CHARVAL',
    'STRINGVAL',
    'EQ',  # Equal comparison
    'NE',  # Not equal comparison
    'LT',  # Less than
    'GT',  # Greater than
    'LE',  # Less than or equal
    'GE',  # Greater than or equal
    'NOT',
    'AND',
    'OR',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'\%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'\='
t_RBRACE = r'\}'
t_LBRACE = r'\{'
t_SEMI = r'\;'
t_COMMA = r','
t_EQ = r'\=='
t_NE = r'\!='
t_LT = r'\<'
t_GT = r'\>'
t_LE = r'\<='
t_GE = r'\>='
t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')   # Check for reserved words
    return t


def t_NUMBER(t):
    r'-?\d+\.?\d*(f)?'
    if t.value.endswith('f'):
        t.value = float(t.value[:-1])
    else:
        t.value = float(t.value)
    return t


def t_CHARVAL(t):
    r'\'.+\''  # Matches a single character enclosed in single quotes
    t.value = t.value[1:-1]  # Removes the quotes
    return t


def t_STRINGVAL(t):
    r'"[^"]*"'  # Matches any characters except double quotes within double quotes
    t.value = t.value[1:-1]  # Removes the quotes
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Define a rule for skipping whitespace characters
t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
