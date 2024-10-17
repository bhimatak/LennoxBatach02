'''
def Test(lst):
    print("Executed Test Function",lst)
    print(id(lst))
    lst.append(30)
    return

l1 = [1,2,3,4]
print(id(l1))
Test(l1)
print(l1,id(l1))

'''
'''
def TestTuple(t1):
    print(t1, id(t1))
    l1 = list(t1)
    l1[1] = 20
    t1 = tuple(l1)
    return t1


t = (1,2,3,4,5)
print(t, id(t))
t = TestTuple(t)
print(t, id(t))
'''
'''
def sq(x):
    return x*x

l1 = [sq(i) for i in range(1,5)]
print(l1)


def Test1(a=10,b=20):
    print(a,b)
    return a+b

print(Test1(5,3))
print(Test1())
print(Test1(1))

print(Test1(b=20,a=33))


def func1(*args):
    for i in args:
        print(i, type(i))


func1(1,2,3,"bhima")
func1(10)
func1(4,5,6,7,8,9,10)

'''

'''
def dFunc(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)


d1 = {'1':2,'3':4,'5':6}
dFunc(**d1)
'''

#ref = lambda: sts

ref1 = lambda x,y: x*y

print(ref1(3,5))

ref2 = lambda x: True if x%2==0 else False

print(ref2(10))

s1 = " abcd "
s1.strip().upper()
s1.upper()

lst = sorted(map(lambda s: s.strip().upper(),[' Bhima '," amit"]))
print(lst)