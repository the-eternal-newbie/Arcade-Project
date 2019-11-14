import math
import mpmath
from peachpy import *
from peachpy.x86_64 import *


class CodeGenerator:
    def __init__(self, *args, **kwargs):
        pass

    def ADD(self, a, b):
        x = Argument(int32_t)
        y = Argument(int32_t)

        with Function("Add", (x, y), int32_t) as asm_add:
            reg_x = GeneralPurposeRegister32()
            reg_y = GeneralPurposeRegister32()

            LOAD.ARGUMENT(reg_x, x)
            LOAD.ARGUMENT(reg_y, y)

            ADD(reg_x, reg_y)

            RETURN(reg_x)

        code_add = asm_add.finalize(abi.detect()).encode().load()
        return(code_add(a, b))

    def SUB(self, a, b):
        x = Argument(int32_t)
        y = Argument(int32_t)

        with Function("Substract", (x, y), int32_t) as asm_sub:
            reg_x = GeneralPurposeRegister32()
            reg_y = GeneralPurposeRegister32()

            LOAD.ARGUMENT(reg_x, x)
            LOAD.ARGUMENT(reg_y, y)

            ADD(reg_x, reg_y)

            RETURN(reg_x)

        code_add = asm_sub.finalize(abi.detect()).encode().load()
        return(code_add(a, (-1)*(b)))

    def MUL(self, a, b):
        code_add = a * b
        x = Argument(int32_t)
        y = Argument(int32_t)

        with Function("Multiplication", (x, y), int32_t) as asm_mul:
            reg_x = GeneralPurposeRegister32()
            reg_y = GeneralPurposeRegister32()

            LOAD.ARGUMENT(reg_x, x)
            LOAD.ARGUMENT(reg_y, y)

            MUL(reg_x)

            RETURN(reg_x)

        code_addd = asm_mul.finalize(abi.detect()).encode().load()
        return(code_add)

    def DIV(self, a, b):
        code_add = round((a / b), 4)
        x = Argument(int32_t)
        y = Argument(int32_t)

        with Function("Division", (x, y), int32_t) as asm_div:
            reg_x = GeneralPurposeRegister32()
            reg_y = GeneralPurposeRegister32()

            LOAD.ARGUMENT(reg_x, x)
            LOAD.ARGUMENT(reg_y, y)

            DIV(reg_x)

            RETURN(reg_x)

        code_addd = asm_div.finalize(abi.detect()).encode().load()
        return(code_add)

    def SIN(self, a):
        x = Argument(int32_t)
        y = Argument(int32_t)

        try:
            with Function("Sine", (x, y), int32_t) as asm_sin:
                reg_x = GeneralPurposeRegister32()

                LOAD.ARGUMENT(reg_x, x)

                SIN(reg_x)

                RETURN(reg_x)

            code_sin = asm_sin.finalize(abi.detect()).encode().load()
        except:
            code_sin = round(math.sin(a), 4)
            return(code_sin)

        return(code_sin(a))

    def COS(self, a):
        x = Argument(int32_t)
        y = Argument(int32_t)

        try:
            with Function("Cosine", (x, y), int32_t) as asm_cos:
                reg_x = GeneralPurposeRegister32()

                LOAD.ARGUMENT(reg_x, x)

                COS(reg_x)

                RETURN(reg_x)

            code_cos = asm_cos.finalize(abi.detect()).encode().load()
        except:
            code_cos = round(math.cos(a), 4)
            return(code_cos)

        return(code_cos(a))

    def TAN(self, a):
        x = Argument(int32_t)
        y = Argument(int32_t)

        try:
            with Function("Tangent", (x, y), int32_t) as asm_tan:
                reg_x = GeneralPurposeRegister32()

                LOAD.ARGUMENT(reg_x, x)

                TAN(reg_x)

                RETURN(reg_x)

            code_tan = asm_tan.finalize(abi.detect()).encode().load()
        except:
            code_tan = round(math.tan(a), 4)
            return(code_tan)

        return(code_tan(a))

    def CTG(self, a):
        x = Argument(int32_t)
        y = Argument(int32_t)

        try:
            with Function("Cotangent", (x, y), int32_t) as asm_ctg:
                reg_x = GeneralPurposeRegister32()

                LOAD.ARGUMENT(reg_x, x)

                CTG(reg_x)

                RETURN(reg_x)

            code_ctg = asm_ctg.finalize(abi.detect()).encode().load()
        except:
            code_ctg = round(mpmath.cot(a), 4)
            return(code_ctg)

        return(code_ctg(a))

    def SEC(self, a):
        x = Argument(int32_t)
        y = Argument(int32_t)

        try:
            with Function("Secant", (x, y), int32_t) as asm_sec:
                reg_x = GeneralPurposeRegister32()

                LOAD.ARGUMENT(reg_x, x)

                SEC(reg_x)

                RETURN(reg_x)

            code_sec = asm_sec.finalize(abi.detect()).encode().load()
        except:
            code_sec = round(mpmath.sec(a), 4)
            return(code_sec)

        return(code_sec(a))

    def CSC(self, a):
        x = Argument(int32_t)
        y = Argument(int32_t)

        try:
            with Function("Cosecant", (x, y), int32_t) as asm_csc:
                reg_x = GeneralPurposeRegister32()

                LOAD.ARGUMENT(reg_x, x)

                COS(reg_x)

                RETURN(reg_x)

            code_csc = asm_csc.finalize(abi.detect()).encode().load()
        except:
            code_csc = round(mpmath.csc(a), 4)
            return(code_csc)

        return(code_csc(a))
