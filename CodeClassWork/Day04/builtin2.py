from builtIn1 import f1
#Defining Modules
def f3():
    print("f3")
def f4():
    print("f4")

if __name__ == "__main__":
    print("\nModule2", dir())
    print("value of __name__: ",__name__)
    # builtIn1.f1()
    # builtIn1.f2()
    print("value of __name__: ", __doc__)

    f1()
    f3()
    f4()