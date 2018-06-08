import sys
import os
import math
from math import sqrt

print("The command line arguments are: ")
for i in sys.argv:
    print(i)

print(os.getcwd())

print(math.sqrt(4))
print(sqrt(9))

if __name__=='__main__':
    print("I am running myself")
else:
    print("Ah! I have been called by other")