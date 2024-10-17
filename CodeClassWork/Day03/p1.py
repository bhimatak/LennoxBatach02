l1 = [5,7,1,2,3,4]
l2 = list()

l1.append(20)
l1.append(30)
print(l1)

l1.remove(20)
print(l1)
#l1.remove(20) # valueerror


print(l1)
l1.sort(reverse=True)
print(l1)


l1 = [1,2,1,2,1,2,3,2,1]

print(l1.count(2))

print(l1)
l1.pop()
print(l1)
l1.pop(1)
print(l1)
l2 = l1

# l1.clear()
# print(l1)

# del l1
print(l2)

l1.pop()
if (l1 is l2):
    print("True")
else:
    print("False")
# print(l1,l2)

l3 = list(l1)

if (l1 is l3):
    print("True")
else:
    print("False")
print(l3)

l1 = list()
l1.extend(range(10))
print(l1)

l2 = ['1']*10
print(l2)