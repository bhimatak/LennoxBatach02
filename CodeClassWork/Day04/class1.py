'''
oops

'''

class Person:
    #class variables
    # Name="Bhima"
    # Age = 45
    # Gender = "M"

    def __init__(self,name,phno,g):
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

    def setProperties(self):
        


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

