class Emp:
    empCount=0

    def __init__(self):
        self.__id=0
        print("Const Invoked")

    def getEmpCount(self):
        return self.empCount

    def setID(self):
        self.__id = 10

    def getID(self):
        return self.__id

    def __incCount(self,pInc):
        self.__id += pInc

    def setCount(self,pi):
        self.__incCount(pi)

e1 = Emp()
Emp.empCount +=1

print(e1.getEmpCount())
e2 = Emp()
Emp.empCount += 1
e3 = Emp()
Emp.empCount += 1
print(e1.getEmpCount())
e1.setID()
print(e1.getID())
e1.setCount(5)
print(e1.getID())
e1.setCount(15)
print(e1.getID())