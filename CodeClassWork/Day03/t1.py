class A:
    def __init__(self,id,name):
        self._id = id
        self._name = name

    def __str__(self):
        s1 = "\nid: "+str(self._id)+"\nname: "+self._name
        return (s1)
class B:
    def __init__(self,age,phno):
        self._age = age
        self._phno = phno
    def __str__(self):
        s1 = "\nage: "+str(self._age)+"\nphone: "+str(self._phno)
        return (s1)

class C(A,B):
    def __init__(self,id,name,age,phno,address):
        self._address = address
        A.__init__(self,id,name)
        B.__init__(self,age,phno)

    def __str__(self):
        s1 = A.__str__(self)+B.__str__(self)+"\naddress: "+str(self._address)
        return s1


c = C(101,"Bhima",34,8888,"GLB")
print(c)
