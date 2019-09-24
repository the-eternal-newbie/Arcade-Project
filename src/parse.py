from lex import tokens
import ply.yacc as yacc

precedence = (
    ('right', 'ID', 'CALL', 'BEGIN', 'IF', 'WHILE'),
    ('right', 'PROCEDURE'),
    ('right', 'VAR'),
    ('right', 'ASSIGN'),
    ('right', 'UPDATE'),
    ('left', 'NE'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'ODD'),
    ('left', 'LPARENT', 'RPARENT'),
)


def p_program(p):
    '''program : block'''
    print("program > Start of program")


def p_block(p):
    '''block : constDecl varDecl procDecl statement'''
    print("block > Code Block")


def p_constDecl(p):
    '''constDecl : CONST constAssignmentList SEMICOLON'''
    print("constDecl > Constant declaration")


def p_constDeclEmpty(p):
    '''constDecl : empty'''
    print("null > End of constDecl")


def p_constAssignmentList1(p):
    '''constAssignmentList : ID ASSIGN NUMBER'''
    print("constAssignmentList > Assignment for integer")


def p_constAssignmentList2(p):
    '''constAssignmentList : constAssignmentList COMMA ID ASSIGN NUMBER'''
    print("constAssignmentList > Assignment for multiple constants")


def p_varDecl1(p):
    '''varDecl : VAR identList SEMICOLON'''
    print("varDecl > Variable declaration")


def p_varDeclEmpty(p):
    '''varDecl : empty'''
    print("null > End of varDecl")


def p_identList1(p):
    '''identList : ID'''
    print("identList > Identifier")


def p_identList2(p):
    '''identList : identList COMMA ID'''
    print("identList > Multiple identifiers")


def p_procDecl1(p):
    '''procDecl : procDecl PROCEDURE ID SEMICOLON block SEMICOLON'''
    print("procDecl > Procedure declaration")


def p_procDeclEmpty(p):
    '''procDecl : empty'''
    print("null > End of procDecl")


def p_statement1(p):
    '''statement : ID UPDATE expression'''
    print("statement > Update expression")


def p_statement2(p):
    '''statement : CALL ID'''
    print("statement > Call of identifier")


def p_statement3(p):
    '''statement : BEGIN statementList END'''
    print("statement > Begin-end structure")


def p_statement4(p):
    '''statement : IF condition THEN statement'''
    print("statement > IF conditional statement")


def p_statement5(p):
    '''statement : WHILE condition DO statement'''
    print("statement > WHILE loop statement")


def p_statementEmpty(p):
    '''statement : empty'''
    print("null > End of statement")


def p_statementList1(p):
    '''statementList : statement'''
    print("statementList > Statement declaration")


def p_statementList2(p):
    '''statementList : statementList SEMICOLON statement'''
    print("statementList > Multiple statement declaration")


def p_condition1(p):
    '''condition : ODD expression'''
    print("condition > Logical expression ODD")


def p_condition2(p):
    '''condition : expression relation expression'''
    print("condition > Logical relation expression")


def p_relation1(p):
    '''relation : ASSIGN'''
    print("relation > Assign symbol")


def p_relation2(p):
    '''relation : NE'''
    print("relation > Not equal symbol")


def p_relation3(p):
    '''relation : LT'''
    print("relation > Less than symbol")


def p_relation4(p):
    '''relation : GT'''
    print("relation > Greater than symbol")


def p_relation5(p):
    '''relation : LTE'''
    print("relation > Less than equal symbol")


def p_relation6(p):
    '''relation : GTE'''
    print("relation > Greater than equal symbol")


def p_expression1(p):
    '''expression : term'''
    print("expresion > Simple term")


def p_expression2(p):
    '''expression : addingOperator term'''
    print("expresion > Adding operator term")


def p_expression3(p):
    '''expression : expression addingOperator term'''
    print("expresion > Adding espression term")


def p_addingOperator1(p):
    '''addingOperator : PLUS'''
    print("addingOperator > Plus symbol")


def p_addingOperator2(p):
    '''addingOperator : MINUS'''
    print("addingOperator > Minus symbol")


def p_term1(p):
    '''term : factor'''
    print("term > Factor")


def p_term2(p):
    '''term : term multiplyingOperator factor'''
    print("term > Multiplying operator factor")


def p_multiplyingOperator1(p):
    '''multiplyingOperator : TIMES'''
    print("multiplyingOperator > Multiply symbol")


def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    print("multiplyingOperator > Divide symbol")


def p_factor1(p):
    '''factor : ID'''
    print("factor > Factor identifier")


def p_factor2(p):
    '''factor : NUMBER'''
    print("factor > Factor number")


def p_factor3(p):
    '''factor : LPARENT expression RPARENT'''
    print("factor > Expression with parenthesis")


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    print("Syntax Error", p)
    print("Error in line " + str(p.lineno))


parser = yacc.yacc()
