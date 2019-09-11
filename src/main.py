import lexer
import parser_lib

if __name__ == '__main__':
    # Start reading snippet code file for compiling
    content = ''
    with open('test.arcd', 'r') as file:
        content = file.read()

    #
    # Lexer Section
    #

    # Initializing Lexer class
    lex = lexer.Lexer(content)
    # Calling lexer method "tokenize" to obtain the tokens in the source code
    lex.tokenize()
    tokens = lex.get_tokens()
    print(tokens)
    #parser = parser_lib.Parser(tokens)
    # parser.parse()
    pass
