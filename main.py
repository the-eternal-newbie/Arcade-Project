import os
import lex

if __name__ == "__main__":
    with open('test.arcd', 'r') as file:
        source_code = file.read()

    lexer = lex.lexer
    lexer.input(source_code)

    while(True):
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    pass
