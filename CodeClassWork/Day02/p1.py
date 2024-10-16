'''
a = 10
b = 10.5
c = "Hello"
d = True
'''
#print(type(a), type(b),type(c), type(d))
'''
a = 'str1'
b = "str1"
'''
#
# c = ''' This is Python Prg class
# Bhima is our tutor


# print(c)
# '''
'''
control sts

1. if 
2. if else
3. if elif else => else if ladder
'''

a = 100
b = 20
c = 300
'''
if (cond):
    braching sts
'''
'''
if (a>b):
    print("True")
    print("t1")
    print("t2")
else:
    print("False")
    print("f1")
    print("f2")
'''
'''
if a>b:
    if a>c:
        print("A")
    else:
        print("C")
    print("Hello")

else:
    if b>c:
        print("B")
    else:
        print("C")

'''
'''
if a>b:
    print("1")
elif a>c:
    print("2")
elif b>c:
    print("3")
else:
    print("4")

print("End Program")

'''

'''
control sts for looping
1. while
2. for

while (cond):
    sts in while block
    
for var in iterableObj:
    sts in for block
    
'''
'''
i = 0

while (i<10):
    print(i, end=" ")
    i+=2
# print()
'''
'''
def test1(a):
    # a += 10
    print(a)

startRange = 1
endRange = 10
stepCount = 1

l1 = [10,20,30,55,77,99]
print(len(l1))
for j in range(len(l1)):
    test1(l1[j])
print()
print("End of Program")

print(type(l1))
for i in l1:
    print(i)
    
'''
'''
a = 5
b = 10

if ((a&1)==1) and ((b>>1)==5):
    print("Hello")

'''

s1 = "hello"

print(s1[len(s1)-1])
print(s1[-1])
startRange = 0
endRange = len(s1)
print(s1[startRange:endRange])
print(s1[0:100:1])

for i in range(len(s1)+1):
    print(i, s1[i])

