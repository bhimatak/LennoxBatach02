'''
list sequence

'''

l1 = []

print(type(l1))

l2 = [123, "hello",10.5,True]
print(type(l2), len(l2))

for i in range(len(l2)):
    print(l2[i])

print(l2[3:0:])

l1 = [1,2,3,4,5]
l2 = [10,11,12,13,14]

l3 = l1+l2
print(type(l3), l3)

l4 = l1*5
print(type(l4), l4)

l1[2] = 30
print(l1)

l1[1:4] = [25,50,75]
print(l1)

l1 = [11,21,31,41,51]

del l1[1:3]
print(l1)

# l1 = [1,2,3,4,5,"ABC"]
print(sum(l1))

s1 = "Hello World123"
l1 = list(s1)
print(type(l1), l1)

l2 = [3,2,5,1,6,4]
print(sorted(l2))

l2.append(101)
print(l2)

l1 = list()
l1.append(100)
l1.append(101)
print(l1)
l1.append("Hello")
print(l1)
l1.append(l2)
print(l1)
print(len(l1))

for i in l1:
    print(i, type(i))

'''    
WAP to add all the odd and even values from s to e and
store in the list in such a way that 1 half of the list
should contain only odd elements and 2nd half of the
same list should contain even elements
and print it
s = 1
e = 10
o/p
l1[0]=1
l1[1]=3
l1[2]=5
l1[3]=7
l1[4]=9
l1[5]=2
l1[6]=4
l1[7]=6
l1[8]=8


'''