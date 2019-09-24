from os import system, name, remove, walk, rmdir, path
from lex import lexer
from parse import parser


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def delete_temp_files():
    for root, dirs, files in walk("__pycache__", topdown=False):
        for name in files:
            remove(path.join(root, name))
        for name in dirs:
            rmdir(path.join(root, name))
    rmdir("__pycache__")
    remove("parser.out")
    remove("parsetab.py")


def lexing(source_code):
    lexer.input(source_code)
    while(True):
        tok = lexer.token()
        if not tok:
            break
        print(tok)


def parsing(source_code):
    parser.parse(source_code)


if __name__ == "__main__":
    while(True):
        clear()
        file_name = str(input("Type source code name to compile: "))
        file_name += ".arcd"

        with open("../test/" + file_name, 'r') as file:
            source_code = file.read()

        print("Selected file {}. What do you wanna do?".format(file_name))
        print("\n1. Lexical Analysis\n2. Syntactical Analysis\n")

        while(True):
            analysis = str(input("Please enter the option number: "))
            if(analysis == "1"):
                lexing(source_code)
                break
            elif(analysis == "2"):
                parsing(source_code)
                break

        delete_temp_files()
        decision = str(input("Do you want to try another file? (y/n): "))
        if(decision != "y"):
            break
