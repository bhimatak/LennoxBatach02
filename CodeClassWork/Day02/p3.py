'''
list sequence

'''

l1 = []

print(type(l1))

l2 = [123, "hello",10.5,True]
print(type(l2), len(l2))

for i in range(len(l2)):
    print(l2[i])

print(l2[::-1])
