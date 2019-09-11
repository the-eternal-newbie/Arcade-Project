import re


class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens_index = 0

    def parse(self):
        index = 0
        for token in self.tokens:
            token_type = token[0]
            token_value = token[1]

            if(token_type == 'VAR_DECLARATION'):
                if(re.match("^[a-zA-Z_][a-zA-Z_0-9]*$", token_value)):
                    self.parse_var_declaration(self.tokens[index:len(self.tokens)])

        index += 1
    def parse_var_declaration(self, token_stream):
        tokens_checked = 0

        for token in range(0, len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            if(token == 0):
                print("Variable type: " + token_value)
            elif(token == 1 and token_type == "IDENTIFIER"):
                print("Variable name: " + token_value)
            elif(token == 1 and token_type != "IDENTIFIER"):
                print("ERROR: Invalid variable name '" + token_value + "'")
                quit()
