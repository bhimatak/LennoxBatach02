import sys

import os

print("Path: ",sys.path)

print("Platform: ", sys.platform)

print("Arguments: ", sys.argv)

CWD = os.getcwd()

print("path: ", CWD)

f_d = os.listdir(".")
print(f_d)