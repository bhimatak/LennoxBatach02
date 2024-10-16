s1 = "hello"
s2 = "world"
s3 = r"Hello\n World"

print('wo' not in s2)
print(s3)

print("All the strings %s %s %s"%(s1,s2,s3))

s4 = s1.upper()+s2.upper()
print(s1.upper()+s2.upper())
print(len(s1),s1.upper(),s4)

s5 = "Java is OOP language. Java is suited for AI and ML"
s6 = s5.replace("a", "G")
print(s6)

s7 = s5.split()
print(type(s7))
print(s7)

for i in s7:
    print(i)

s8 = s5.split(sep=".")
print(s8)

str1 = "Python os a Programmig language"

print(str1[7])
idx = str1.find("a",11,16)
idx = str1.find("Z")

print(idx)
# idx1 = str1.index("Z")
# print(idx1)

s10 = "Python 1234"

print(s10.isalnum())