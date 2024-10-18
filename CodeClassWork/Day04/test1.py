class A:
    def __init__(self):
        self._a = 0
    def setA(self):
        self._a = 10
    def getA(self):
        return self._a

class B(A):
    def __init__(self):
        super().__init__()
        self._b = 20
