import ply.yacc as yacc
import os
import codecs
import re
from lex import tokens
from sys import stdin

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
    '''program = block'''
    print("program")
    #p[0] = program(p[1], "program")


def p_varDecl(p):
    '''varDecl = VAR_DECLARATION varAssignmentList;'''
    print("varDecl")
    #p[0] = varDecl(p[2])


def p_varDeclEmpty(p):
    '''varDecl = empty'''
    print("null")
   # p[0] = Null()
