from assambler import CodeGenerator

if __name__ == "__main__":
    compile_code = CodeGenerator()
    print(compile_code.SIN(2))
    print(compile_code.COS(2))
    print(compile_code.TAN(2))
    print(compile_code.CTG(2))
    print(compile_code.SEC(2))
    print(compile_code.CSC(2))
    pass
