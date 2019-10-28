txt = " "
cont = 0


def increaseCounter():
    global cont
    cont += 1
    return("%d" % cont)


class Node():
    pass


class Null(Node):
    def __init__(self):
        self.type = 'void'

    def display(self, ident):
        print(ident + "Node null")

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id+"[label= "+"Node_null"+"]"+"\n\t"

        return(id)


class program(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"

        return("digraph G {\n\t"+txt+"}")


class block(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def display(self, ident):
        if(type(self.son1) == type(tuple())):
            self.son1[0].display(" "+ident)
        else:
            self.son1.display(" "+ident)

        if(type(self.son2) == type(tuple())):
            self.son2[0].display(" "+ident)
        else:
            self.son2.display(" "+ident)

        if(type(self.son3) == type(tuple())):
            self.son3[0].display(" "+ident)
        else:
            self.son3.display(" "+ident)

        if(type(self.son4) == type(tuple())):
            self.son4[0].display(" "+ident)
        else:
            self.son4.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        if(type(self.son1) == type(tuple())):
            son1 = self.son1[0].translate()
        else:
            son1 = self.son1.translate()

        if(type(self.son2) == type(tuple())):
            son2 = self.son2[0].translate()
        else:
            son2 = self.son2.translate()

        if(type(self.son3) == type(tuple())):
            son3 = self.son3[0].translate()
        else:
            son3 = self.son3.translate()

        if(type(self.son3) == type(tuple())):
            son4 = self.son4[0].translate()
        else:
            son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return(id)


class constDecl(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)
        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        if(type(self.son1) == type(tuple())):
            son1 = self.son1[0].translate()
        else:
            son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + "->"+son1+"\n\t"

        return(id)


class constAssignmentList1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)
        self.son3.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return(id)


class constAssignmentList2(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)
        self.son3.display(" "+ident)
        self.son4.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return(id)


class varDecl1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class identList1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class identList2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return(id)


class procDecl1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def display(self, ident):

        if(type(self.son1) == type(tuple())):
            self.son1[0].display(" "+ident)
        else:
            self.son1.display(" "+ident)

        self.son2.display(" "+ident)
        self.son3.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return(id)


class statement1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)
        self.son3.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return(id)


class statement2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class statement3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class statement4(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def display(self, ident):
        self.son1.display(" "+ident)

        if(type(self.son2) == type(tuple())):
            self.son2[0].display(" "+ident)
        else:
            self.son2.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return(id)


class statement5(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def display(self, ident):
        self.son1.display(" "+ident)

        if(type(self.son2) == type(tuple())):
            self.son2[0].display(" "+ident)
        else:
            self.son2.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return(id)


class statementList1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class statementList2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return(id)


class condition1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class condition2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)
        self.son3.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return(id)


class relation1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class relation2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class relation3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class relation4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class relation5(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class relation6(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class expression1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class expression2(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return(id)


class expression3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)
        self.son3.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return(id)


class addingOperator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class addingOperator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class term1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class term2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def display(self, ident):
        self.son1.display(" "+ident)
        self.son2.display(" "+ident)
        self.son3.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return(id)


class multiplyingOperator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class multiplyingOperator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class factor1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class factor2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class factor3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def display(self, ident):
        self.son1.display(" "+ident)

        print(ident + "Node: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        son1 = self.son1.translate()

        txt += id + "[label= "+self.name+"]"+"\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return(id)


class Id(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"ID: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= "+self.name+"]"+"\n\t"

        return(id)


class Assign(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):

        print(ident+"Assign: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class NE(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"NE: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class LT(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"LT: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class GT(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"GT: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class LTE(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"LTE: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class GTE(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"GTE: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class Plus(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"Plus: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class Minus(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"Minus: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id


class Times(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"Times: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class Divide(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"Divide: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class Update(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"Update: "+self.name)

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return(id)


class Number(Node):
    def __init__(self, name):
        self.name = name

    def display(self, ident):
        print(ident+"Number: "+str(self.name))

    def translate(self):
        global txt
        id = increaseCounter()
        txt += id + "[label= "+str(self.name)+"]"+"\n\t"

        return(id)

# class empty(Node):
# 	def __init__(self,name):
# 		pass
