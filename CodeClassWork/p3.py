'''
looping sts

'''
'''
i=11

while(i<=10):
    print(i)
    i+=1
print("End of Program")

'''

l1 = [11,21,31,41,53]
a = 22
for i in range(1,10,2):
    print(i)

s1 = "Hello"
'''
print("string1", end="\r")
print("string2",end="*")
print("string3")
'''
'''
s1="a1"
s2="a2"
s3="a3"

print("string1", sep=",", end=" ")
print("string2",sep=" ",end=" ")
print("string3")

print(s1,s2,s3,"Hello World", sep=",")
'''
'''
a,b,c = int(input("Enter 3 values: "))

print(a,  type(a))
print(b,  type(b))
print(c,  type(c))
'''
# 0,3,8,15....

n = int(input())
'''
for i in range(1,n+1):
    if (i%n == 0):
        print((i * i) - 1)
    else:
        print((i*i)-1, end=",")

# for i in range(n,101,2):
#     print(i)

'''

# for i in range(1,n+1):
#     print("*"*n)

#printf("%c",65)=>A

print(chr(65))
str1 = ""
l1 = list()
l1 = [chr(i) for i in range(65,69)]
print(l1)