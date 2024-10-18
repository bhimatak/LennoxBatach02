'''
try:
    z = 10/0
except ZeroDivisionError as e:
    print(e)
'''

try:
    '''
    file = open("file1.txt","r")
    content = file.read()
    print(type(content), content)
    file.close()
    file2 = open("file2.txt", "w+")
    # file2.write(content)
    file2.close()
    '''
    with open("file1.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(e)
finally:
    print("done with opening and reading of file")
