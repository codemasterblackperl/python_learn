
def say_hello():
    print("Hello")

say_hello()

#this wont work because hello1 is not yet known to the program so always do the function before calling it
#say_hello1()

#def say_hello1():
#    print("Hello")

def print_max(a,b):
    if(a>b):
        print(a," is greater than ",b)
    elif(a==b):
        print(a," is equal to ",b)
    else:
        #you can left only one space too if you dont want to use a tab
        print(a," is less than ",b)

print_max(5,5)

y=5

def print_x(x):
    #global will change the value globally
    global y
    print(x)
    #this will only change the value of x localy so main value of x remains same as it before
    x=2
    y=2
    print("y is now ",y)
    print("x is now ",x)

x=5
print(y)
print_x(x)
print("after executing function now x is ",x)
print("after executing function now y is ",y)