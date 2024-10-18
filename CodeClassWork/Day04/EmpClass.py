class Person:
    def __init__(self,name="",age=0,address=""):
        self._name = name
        self._age = age
        self._address = address

    def setValuePerson(self):
        print("\nEnter ")
        self._name = input("Name: ")
        self._age = int(input("Age: "))
        self._address = input("Adress: ")

    def printPerson(self):
        print("\nDetails are")
        print("{}\n{}\n{}".format(self._name,self._age,self._address))

class Employee(Person):

    def __init__(self, id=0,sal=0):
        super().__init__()
        self._id = id
        self._salary = sal
        self._roles

    def setEmployee(self):
        self.setValuePerson()
        self._id = int(input("ID: "))
        self._salary = int(input("Salary: "))

    def printEmployee(self):
        self.printPerson()
        print("{}\n{}".format(self._id,self._salary))



class Manager(Employee):
    def Approval(self):
        pass
class TL(Employee):
    pass
class Developers(Employee):
    pass

e1 = Employee()
e1.setEmployee()
e1.printEmployee()
