def f1():
    #calling f1
    print("Hello f1")

def f2():
    print("Hello f2")

if __name__ == "__main__":
    f1()
    f2()
    print("\nModule1\n",dir())
    print("value of __name__: ",__name__)
