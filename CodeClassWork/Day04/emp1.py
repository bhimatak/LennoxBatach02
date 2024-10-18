class Employee:

    def __init__(self, id=0,fname="",lname=""):
        self._id = id
        self._fName = fname
        self._lName = lname

    def setlname(self,lname):
        self._lName =lname

    def getID(self):
        return self._id

    def display(self):
        print("Employee Record\n{}\n{}\n{}\n".format(self._id,self._fName,self._lName))

e1 = Employee(101,"Bhima1","Shankar1")
e2 = Employee(102,"Bhima2","Shankar2")
e3 = Employee(103,"Bhima3","Shankar3")
l =[]

for i in [e1,e2,e3]:
    i.display()
    l.append(i.getID())

print(l)


# id = int(input("Enter id: "))
# for i in range(3):
#     if id == e1