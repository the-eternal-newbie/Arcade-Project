import ply.yacc as yacc
import os
import codecs
import re
from lex import tokens
from sys import stdin

precedence = (
    (),
    (),
)
