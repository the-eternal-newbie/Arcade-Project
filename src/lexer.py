import re


class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

        # Dictionary for words and digits matching
        self.regex_dict = {
            "^[-+]?\d+$": "INTEGER",
            "^[-+]?\d*\.?\d*$": "FLOAT",
            "^(\w*)$": "IDENTIFIER"
        }

        # Dictionary for reserved words matching
        self.reserved_words_dict = {
            "start": "RESERVED_WORD",
            "var": "VAR_DECLARATION",
            "meta": "STRUCTURE_DECLARATION",
            "if": "CONDITIONAL_STATEMENT",
            "not": "CONDITIONAL_STATEMENT",
            "switch": "CONDITIONAL_STATEMENT",
            "stop": "",
            "error": "",
            "default": "",
            "doFor": "FOR_ITERATION",
            "doWhile": "DO_ITERATION",
            "print": "OUTPUT",
            "read": "INPUT"
        }

        # Dictionary for operators matching
        self.operators_dict = {
            "=": "OPERATOR",
            "+": "OPERATOR",
            "-": "OPERATOR",
            "*": "OPERATOR",
            "/": "OPERATOR",
            "%": "OPERATOR",
            "^": "OPERATOR",
            "--": "OPERATOR",
            "++": "OPERATOR",
            "+=": "OPERATOR",
            "-=": "OPERATOR",
            "*=": "OPERATOR",
            "/=": "OPERATOR",
            "^=": "OPERATOR",
            "==": "OPERATOR",
            ">": "OPERATOR",
            "<": "OPERATOR",
            "<=": "OPERATOR",
            ">=": "OPERATOR",
        }

    def tokenize(self):

        # Tokens' storage
        tokens = []

        # This is a word list of the source code
        source_code = self.source_code.split()

        # We iterate through the entire source code words list
        for wordcode in source_code:
            boolean = False
            word = wordcode

            # If the word in the list includes a semicolon at the end, then it must be an end statement
            # so we rip off the semicolon from the word and put the boolean flag ON
            if wordcode[-1] == ";":
                boolean = True
                word = wordcode[:-1]

            # if the word is found in the reserved words dictionary, it's recognized as a reserved word
            # and we create an identifier token for it and so on with the other cases
            if word in self.reserved_words_dict:
                tokens.append([self.reserved_words_dict[word], word])
            elif word in self.operators_dict:
                tokens.append([self.operators_dict[word], word])
            else:
                for key in self.regex_dict:
                    if re.match(key, word):
                        tokens.append([self.regex_dict[key], word])
                        break

            # If the flag is ON it means that the word has a semicolon, therefore it must be an end statement
            if boolean:
                tokens.append(["END_STATEMENT", ";"])

        print(tokens)
