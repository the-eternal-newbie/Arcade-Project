from os import system, name, remove, walk, rmdir, path
from sys import stdin
from lex import lexer
from parse import parser
from parse_semantic import parser_semantic
from assambler import CodeGenerator


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def delete_temp_files(semantic=False):
    for root, dirs, files in walk("__pycache__", topdown=False):
        for name in files:
            remove(path.join(root, name))
        for name in dirs:
            rmdir(path.join(root, name))
    rmdir("__pycache__")
    remove("parser.out")
    remove("parsetab.py")
    if(semantic):
        remove("graphvizthree.vz")


def read_file():
    file_name = str(input("Type source code name to compile: "))
    file_name += ".arcd"

    with open("../test/" + file_name, 'r') as file:
        source_code = file.read()

    return(file_name, source_code)


def write_file():
    file_name = str(input("Please enter a name for the new file: "))
    file_name += ".arcd"
    source_code = ""
    print("OK! {} created, start writing coude!".format(file_name))
    try:
        file = open("../test/" + file_name, 'w+')
        for line in stdin:
            source_code += line + "\n"
            file.write(line)
    except(KeyboardInterrupt):
        file.close()
        clear()
        return(file_name, source_code)


def translate(result):
    graphFile = open('graphvizthree.vz', 'w')
    graphFile.write(result.translate())
    graphFile.close()
    print("The translated program has been saved as \"graphvizthree.vz\"")


def lexing(source_code):
    lexer.input(source_code)
    while(True):
        tok = lexer.token()
        if not tok:
            break
        print(tok)


def parsing(source_code):
    parser.parse(source_code)


def semantic(source_code):
    result = parser_semantic.parse(source_code, debug=True)
    translate(result)


def generator(file_name, source_code):
    clear()
    compile_code = CodeGenerator()
    result = "Compiled Successfully: "
    print(source_code)
    with open("../test/" + file_name, 'r') as file:
        for line in file:
            for word in line.split():
                if(":=" in word):
                    op = word[3:-1]
                    if("sin" in op):
                        result += str(compile_code.SIN(int(op[4:-1]))) + ", "

                    if("cos" in op):
                        result += str(compile_code.COS(int(op[4:-1]))) + ", "

                    if("tan" in op):
                        result += str(compile_code.TAN(int(op[4:-1]))) + ", "

                    if("sec" in op):
                        result += str(compile_code.SEC(int(op[4:-1]))) + ", "

                    if("ctg" in op):
                        result += str(compile_code.CTG(int(op[4:-1]))) + ", "

                    if("csc" in op):
                        result += str(compile_code.CSC(int(op[4:-1]))) + ", "

                    if("+" in op):
                        pos = op.find("+")
                        operator = int(op[0:pos])
                        operand = int(op[pos+1:])
                        result += str(compile_code.ADD(operator,
                                                       operand)) + ", "

                    if("-" in op):
                        pos = op.find("-")
                        operator = int(op[0:pos])
                        operand = int(op[pos+1:])
                        result += str(compile_code.SUB(operator,
                                                       operand)) + ", "

                    if("*" in op):
                        pos = op.find("*")
                        operator = int(op[0:pos])
                        operand = int(op[pos+1:])
                        result += str(compile_code.MUL(operator,
                                                       operand)) + ", "

                    if("/" in op):
                        pos = op.find("/")
                        operator = int(op[0:pos])
                        operand = int(op[pos+1:])
                        result += str(compile_code.DIV(operator,
                                                       operand)) + ", "

    print("\n"+result)


if __name__ == "__main__":
    flag = False
    while(True):
        clear()
        print("Welcome to Arcade compiler!\n")

        file_name, source_code = read_file()

        clear()
        print("Selected file {}. What do you wanna do?".format(file_name))
        print("\n1. Lexical Analysis\n2. Syntactical Analysis\n3. Semantic Analysis\n4. Code generation\n")

        while(True):
            analysis = str(input("Please enter the option number: "))
            if(analysis == "1"):
                lexing(source_code)
                break
            elif(analysis == "2"):
                parsing(source_code)
                break
            elif(analysis == "3"):
                flag = True
                semantic(source_code)
                break
            elif(analysis == "4"):
                generator(file_name, source_code)
                break

        decision = str(input("Do you want to try another file? (y/n): "))
        if(decision != "y"):
            delete_temp_files(flag)
            break
