'''
tuples => elements are immutable
t1 = ()

'''

t1 = (1,2,3,4,5)
t2 = (10,20,30,40,50)
print(type(t1), t1)
for i in range(len(t1)):
    print(t1[i])
t3 = t1+t2
print(t3)
t4 = (1,)*5
print(t4)
l2 = list(t1)
print(type(l2),l2)
t5 = tuple(l2)
print(type(t5),t5)


t6 = (7,10,1,2,3,4,5)
print(id(t6))
l1 = list(t6)
l1[2] = 30
print(id(l1))
t6 = tuple(l1)
print(t6)
print(id(t6))

# del t6
# print(t6)

l7 = sorted(t6)
print(sorted(t6))
print(t6,l7)

'''
list comprehensions

l1 = [exp for ele in iterableObj]

'''
l1 = []
a = 0
for i in range(1,10):
    a = a+(i*2)
    l1.append(a)
print(l1)

l2 = [i for i in range(1,10,2)]
print(l2)

lNames = ['bhima', 'shankar','amit']
lNames = [names.upper() for names in lNames]
print(lNames)

l7 = []
for i in range(1,100):
    if (i%2 == 0):
        l7.append(i)
print(l7)

l8 = [i for i in range(1,100) if i%2==0 ]
print(l8)
l9 = [i for i in range(1,100) if i%2==0 ]+[i for i in range(1,100) if i%2!=0 ]
print(l9)

l10 =[]
for i in range(1,10):
    if i%2 == 0:
        l10.append(i+10)
    else:
        l10.append(i+5)
print(l10)

#[resElem for ele in iterObj ]
l11 = [i+10 if i%2==0 else i+5 for i in range(1,10)]
print(l11)

l1 = ['1','2','3']
print(list(map(int, l1)))
# int('3')
a,b,c = map(int,input().split())

print(a,b,c, type(c))

l = map(int, input().split(','))
print(l, type(l))
t2 = tuple(l)
print(t2)
# map(method, iterableObj)
# a,b,c = intinput().split()
# print(type(a),b,c)
# a = int(a)
#
#
#
#
# # s1 = "hello world! Bhima"
# # print(s1.split())
