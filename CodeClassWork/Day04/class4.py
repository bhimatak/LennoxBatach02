class A:
    a = 0
    b = 0

    def __init__(self):
        self.a = 10
        self.b = 20

    def dispValueA(self):
        print(self.a, self.b)

    def setA(self, val1, val2):
        self.a = val1
        self.b = val2


class B(A):
    c = 0
    d = 0

    def __init__(self):
        self.c = 30
        self.d = 40
        A.__init__(self)

    def dispValueB(self):
        print(self.c, self.d)
        self.dispValueA()

    def setB(self, val1, val2):
        self.c = val1
        self.d = val2


x = A()
x.dispValueA()

y = B()
# y.setA(11,12)
y.dispValueB()
y.dispValueA()