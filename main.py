import os
from lex import lexer
from parse import parser


def lexing():
    while(True):
        tok = lexer.token()
        if not tok:
            break
        print(tok)


def parsing(source_code):
    parser.parse(source_code)
    pass


if __name__ == "__main__":
    with open('simple_test.arcd', 'r') as file:
        source_code = file.read()

    # lexer.input(source_code)
    # lexing()
    parsing(source_code)
