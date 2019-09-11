# ------------------------------------------------------------
# lex.py
#
# Tokenizer for Arcade Language
#
# ------------------------------------------------------------
import ply.lex as lex
import re
# List of token names.
tokens = [
    "IDENTIFIER",
    "INTEGER",      # 1234
    "FLOAT",        # 12.34
    "STRING",       # word

    # --------------------------------------------------------
    # OPERATORS
    "PLUS",         # +
    "MINUS",        # -
    "TIMES",        # *
    "DIVIDE",       # /
    "ODD",          # %
    "ASSIGN",       # =
    "POWER",        # ^
    "DECREMENT",    # --
    "INCREMENT",    # ++
    "PLUSEQUAL",    # +=,
    "MINUSEQUAL",   # -=
    "TIMESEQUAL",   # *=
    "DIVIDEEQUAL",  # /=
    "ODDEQUAL",     # %=
    "GREATER",      # >
    "LESS",         # <
    "GREATEREQUAL",  # >=
    "LESSEQUAL",    # <=
    "IDENTICAL",    # ==
    "DIFFERENT",    # !=
    # --------------------------------------------------------

    # --------------------------------------------------------
    # PUNCTUATION
    "COLON",        # :
    "SEMICOLON",    # ;
    "COMMA",        # ,
    "DOT",          # .
    "LPAREN",       # (
    "RPAREN",       # )
    "LBRACKET",     # [
    "RBRACKET",     # ]
    "LCURLY",       # {
    "RCURLY",       # }
    "QUOTES",    # ""
    "COMMENT",      # #
    # --------------------------------------------------------
]

reserved = {
    'if': 'IF_STATEMENT',
    'not': 'IF_NOT_STATEMENT',
    'doWhile': 'WHILE_STATEMENT',
    'doFor': 'FOR_STATEMENT',
    'start': 'START_DECLARATION',
    'var': 'VAR_DECLARATION',
    'meta': 'STRUCT_DECLARATION',
    'switch': 'SWITCH_STATEMENT',
    'error': 'ERROR_SWITCH',
    'default': 'DEFAULT_CASE',
    'print': 'OUT_STREAM',
    'read': 'IN_STREAM'
}

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'%'
t_ASSIGN = r'='
t_POWER = r'\^'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVIDEEQUAL = r'/='
t_ODDEQUAL = r'%='
t_GREATER = r'>'
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_IDENTICAL = r'=='
t_DIFFERENT = r'!='

# Punctuation
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_SEMICOLON = r'\;'
t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'
t_QUOTES = r'"'

# Regular expression rules for specific tokens


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    if(t.value.upper() in reserved):
        t.value = t.value.upper()
        t.type = t.value

    return(t)


def t_INTEGER(t):
    r'[-+]?\d+'
    t.value = int(t.value)
    return(t)


def t_FLOAT(t):
    r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$'
    t.value = float(t.value)
    return(t)


def t_STRING(t):
    r'^[a-zA-Z0-9_ \*,.\-;\+%_\!\?\$]+$'
    t.value = str(t.value)
    return(t)


def t_COMMENT(t):
    r'\#.*'
    pass


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Spacetabs handling


def t_SPACETAB(t):
    r'[ \t]+'
    print("Whitespace or tab")


# Build the lexer
lexer = lex.lex()
