import ply.yacc as yacc
from lex import tokens

precedence = (
    ('right', 'ASSIGN'),
    ('left', 'DIFFERENT', 'IDENTICAL'),
    ('left', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'ODD'),
    ('right', 'INCREMENT', 'DECREMENT'),
    ('right', 'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVIDEEQUAL', 'ODDEQUAL'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'LBRACKET', 'RBRACKET'),
)

# Definding productions


def p_program(p):
    '''program : block'''
    print("program")


def p_block(p):
    '''block : varDecl varAssign statement'''
    print("block")


def p_varDecl1(p):
    '''varDecl : VAR_DECLARATION IDENTIFIER SEMICOLON'''
    print("varDecl 1")


def p_varDecl1(p):
    '''varDecl : VAR_DECLARATION IDENTIFIER ASSIGN INTEGER SEMICOLON'''
    print("varDecl assignment: integer")


def p_varDecl2(p):
    '''varDecl : VAR_DECLARATION IDENTIFIER ASSIGN FLOAT SEMICOLON'''
    print("varDecl assignment: integer")


def p_varDecl3(p):
    '''varDecl : VAR_DECLARATION IDENTIFIER ASSIGN STRING SEMICOLON'''
    print("varDecl assignment: string")


def p_varDecl4(p):
    '''varDecl : VAR_DECLARATION IDENTIFIER ASSIGN BOOLEAN_TRUE SEMICOLON'''
    print("varDecl assignment: bool")


def p_varDecl5(p):
    '''varDecl : VAR_DECLARATION IDENTIFIER ASSIGN BOOLEAN_FALSE SEMICOLON'''
    print("varDecl assignment: bool")


def p_varAssign1(p):
    '''varAssign : IDENTIFIER ASSIGN INTEGER SEMICOLON'''
    print("var assignment: integer")


def p_varAssign2(p):
    '''varAssign : IDENTIFIER ASSIGN FLOAT SEMICOLON'''
    print("var assignment: float")


def p_varAssign3(p):
    '''varAssign : IDENTIFIER ASSIGN STRING SEMICOLON'''
    print("var assignment: string")


def p_varDeclEmpty(p):
    '''varDecl : empty'''
    print("null")


# def p_identList1(p):
#     '''identList : IDENTIFIER'''
#     print("identList 1")


# def p_identList2(p):
#     '''identList : identList COMMA IDENTIFIER'''
#     print("identList 2")


# def p_identListEmpty(p):
#     '''identList : empty'''
#     print("null")


def p_statement1(p):
    '''statement : IDENTIFIER ASSIGN expression SEMICOLON'''
    print("statement 1")


def p_statement2(p):
    '''statement : IF_STATEMENT condition IF_NOT_STATEMENT statement'''
    print("statement 3")


def p_statement3(p):
    '''statement : FOR_STATEMENT LPAREN statement RPAREN COLON statement'''
    print("statement 4")


def p_statement4(p):
    '''statement : WHILE_STATEMENT LPAREN condition RPAREN COLON statement'''
    print("statement 5")


def p_statementEmpty(p):
    '''statement : empty'''
    print("null")


# def p_statementList1(p):
#     '''statementList : statement'''
#     print("statementList 1")


# def p_statementList2(p):
#     '''statementList : statementList SEMICOLON statement'''
#     print("statementList 2")


# def p_statementListEmpty(p):
#     '''statementList : empty'''
#     print("null")


def p_condition(p):
    '''condition : expression relation expression'''
    print("condition")


def p_relation1(p):
    '''relation : IDENTICAL'''
    print("relation 1")


def p_relation2(p):
    '''relation : DIFFERENT'''
    print("relation 2")


def p_relation3(p):
    '''relation : GREATER'''
    print("relation 3")


def p_relation4(p):
    '''relation : LESS'''
    print("relation 4")


def p_relation5(p):
    '''relation : GREATEREQUAL'''
    print("relation 5")


def p_relation6(p):
    '''relation : LESSEQUAL'''
    print("relation 6")


def p_expression1(p):
    '''expression : IDENTIFIER'''
    print("expression 1")


def p_expression2(p):
    '''expression : PLUS IDENTIFIER'''
    print("expression 2")


def p_expression3(p):
    '''expression : expression PLUS IDENTIFIER'''
    print("expression 3")


def p_term1(p):
    '''term : factor'''
    print("term 1")


def p_term2(p):
    '''term : term multiplyingOperator factor'''
    print("term 2")


def p_multiplyingOperator1(p):
    '''multiplyingOperator : TIMES'''
    print("multiplyingOperator 1")


def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    print("multiplyingOperator 2")


def p_factor1(p):
    '''factor : IDENTIFIER'''
    print("factor 1")


def p_factor2(p):
    '''factor : INTEGER'''
    print("factor 2")


def p_factor3(p):
    '''factor : FLOAT'''
    print("factor 3")


def p_factor4(p):
    '''factor : LPAREN expression RPAREN'''
    print("factor 4")


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    print("Syntax Error", p)
    print("Error in line " + str(p.lineno))


# Build the parser
parser = yacc.yacc()
