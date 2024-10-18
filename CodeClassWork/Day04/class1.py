'''
oops

'''

class Person:
    #class variables
    # Name="Bhima"
    # Age = 45
    # Gender = "M"

    def __init__(self,name="",phno=0,g=""):
        #init variables
        print("Constructor Invoked")
        self._fName = name
        self._age = 0
        self._phno = phno
        self._gender= g


    def getName(self):
        return self._fName
    def setName(self,name):
        self._fName = name

    def getPhno(self):
        return self._phno

    def setPhno(self, phno):
        self._phno = phno

    def setGender(self, g):
        self._gender = g

    def getGender(self):
        return  self._gender

    def getAge(self):
        return self._age

    def setProperties(self, name,phno,age,g):
        print("\nSetting the Properties of Person")
        self._fName = name
        self._age =age
        self._phno = phno
        self._gender =g

    def setPropUI(self):
        print("\nEnter Value of Person")
        self._fName = input("Name: ")
        self._phno = int(input("Phno: "))
        self._age = int(input("Age: "))
        self._gender = input("Gender: ")

    def displayPerson(self):
        print("\nPerson Details are\n")
        print("\n{}\n{}\n{}\n{}".format(self._fName,self._phno,self._age,self._gender))




'''        

p1 = Person()

print(p1,id(p1))
print(p1.Name)
p1.Name = "Shankar"
print(p1.Name)
p2 = Person()
print(p2,id(p2))
print(p2.Name)
print(p1.phno)
print("p1 Name: ",p1.getName())
p1.setName("Amit")
print("p1 Name: ",p1.getName())
'''
'''
p1 = Person()
print(p1.getName(), p1.getPhno(), p1.getGender())
p1.setName("Bhima")
p1.setPhno(9999)
p1.setGender("M")
print(p1.getName(), p1.getPhno(), p1.getGender())

p2 = Person()
print(p2.getName(), p2.getPhno(), p2.getGender())
'''
p3 = Person("Bhima",999,"M")
print(p3.getName(), p3.getPhno(), p3.getGender(), p3.getAge())

p3.displayPerson()

p4 = Person()
p4.setProperties("Shankar",888,45,g="M")
p4.displayPerson()
p5 = Person()
p5.setPropUI()
p5.displayPerson()