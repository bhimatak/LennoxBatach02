'''
dict => key and value pair
{}
'''

d1 = {}
print(type(d1))
d2 = dict()
print(type(d2))
d1['key1'] = 'value1'
d1['key2'] = 'value2'
print(d1)
d1['key3'] = 'value3'
print(d1)

print("New Output")
for i in d1:
    print(i, d1[i])
    if i == 'key2':
        d1[i] = "bhima"
        break

print(d1)

d1['key4'] = ['bhima', 'shankar', 'amit']
print(d1)

for i,j in d1.items():
    #
    if type(j) == list or type(j) == tuple:
        for k in j:
            print(i, k)
    else:
        print(i, j)

d1['key5'] = {'10':2,'20':3,'30':4}
print(d1)

for i,j in d1.items():
    #
    if type(j) == list or type(j) == tuple:
        for k in j:
            print(i, k)
    elif type(j) == dict:
        for l,m in j.items():
            print(i,j,l,m)
    else:
        print(i, j)

d3 = {1:2,3:4,5:6,7:8}

for i in d3.items():
    print(i, type(i)) #tuples are generated

'''

returnType NameFunc(args)
{
    return type
}

def NameFunc(args):
    sts
    return dt
'''