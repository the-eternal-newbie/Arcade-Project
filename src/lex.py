import ply.lex as lex

reserved = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'CALL', 'CONST',
            'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE'
            ]

tokens = reserved + ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                     'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
                     'LPARENT', 'RPARENT', 'COMMA', 'SEMICOLON',
                     'DOT', 'UPDATE'
                     ]

t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_DOT = r'\.'
t_UPDATE = r':='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if(t.value.upper() in reserved):
        t.value = t.value.upper()
        t.type = t.value

    return(t)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
