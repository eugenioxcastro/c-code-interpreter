import ply.yacc as yacc
from myLexer import tokens

precedence = (
    ('nonassoc', 'EQ', 'NE', 'LT', 'GT', 'LE', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
)


def p_start(p):
    '''start : PROGRAM MAIN LBRACE body RBRACE'''
    p[0] = p[4]


def p_code(p):
    '''body : declaration_list statement_list'''
    p[0] = (p[1], p[2])


def p_declaration_list(p):
    '''declaration_list : declaration
                        | declaration_list declaration
                        | empty '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])


def p_declaration(p):
    '''declaration : type_specifier variable_list SEMI'''
    p[0] = (p[1], p[2])


def p_type_specifier(p):
    ''' type_specifier : INT
                        | BOOL
                        | STRING
                        | DOUBLE
                        | FLOAT
                        | CHAR '''
    p[0] = p[1].lower()


def p_variable_list(p):
    ''' variable_list : ID
                     | variable_list COMMA ID
                     | assignment '''
    if len(p) == 2:
        if isinstance(p[1], str):
            p[0] = p[1]
        else:
            p[0] = p[1]
    else:
        p[0] = (p[1], p[3])


def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement
                      | empty '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])


def p_statement(p):
    '''statement : assignment SEMI
                 | print SEMI
                 | unary
                 | if_statement
                 | for_statement
                 | while_statement
                 | func_statement_declaration
                 | func_statement_call'''
    p[0] = p[1]
    pass


def p_assignment(p):
    '''assignment : ID EQUAL expression'''
    p[0] = ('=', p[1], p[3])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression'''
    p[0] = (p[2], p[1], p[3])


def p_expression_comparison(p):
    '''expression : expression EQ expression
                   | expression NE expression
                   | expression LT expression
                   | expression GT expression
                   | expression LE expression
                   | expression GE expression'''
    p[0] = (p[2], p[1], p[3])


def p_expression_bool(p):
    '''expression : NOT expression
                  | expression AND expression
                  | expression OR expression'''
    if len(p) == 3:  # NOT operation
        p[0] = (p[1], p[2])
    else:  # AND or OR operation
        p[0] = (p[2], p[1], p[3])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_expression_values(p):
    '''expression : NUMBER
                  | STRINGVAL
                  | CHARVAL
                  | TRUE
                  | FALSE'''
    p[0] = p[1]


def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('var', p[1])


def p_print(p):
    '''print : WRITELN LPAREN expression RPAREN
             | WRITE LPAREN expression RPAREN'''
    p[0] = (p[1], p[3])


def p_unary(p):
    '''unary : ID INCREMENT SEMI
             | ID DECREMENT SEMI
             | ID INCREMENT
             | ID DECREMENT'''
    p[0] = (p[2], p[1])


def p_statement_if(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
                    | IF LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    if len(p) == 12:
        p[0] = ('if_else', p[3], p[6], p[10])
    else:
        p[0] = ('if', p[3], p[6])


def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment SEMI expression SEMI unary RPAREN LBRACE statement_list RBRACE
                     | FOR LPAREN assignment SEMI expression SEMI assignment RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('for', p[3], p[5], p[7], p[10])


def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('while', p[3], p[6])


def p_func_statement_declaration(p):
    '''func_statement_declaration : VOID ID LPAREN RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('func', p[2], p[6])


def p_func_statement_call(p):
    '''func_statement_call : ID LPAREN RPAREN SEMI'''
    p[0] = ('func_call', p[1])


def p_empty(p):
    'empty :'
    p[0] = None


def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc.yacc(start="start")
