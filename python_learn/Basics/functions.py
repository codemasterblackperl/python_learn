
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

#default argument is times
def print_x(x,times=1):
    #global will change the value globally
    global z,y
    print(x)
    #this will only change the value of x localy so main value of x remains same as it before
    z=6
    x=2
    y=2
    print("y is now {0}\r\n".format(y)*times)
    print("x is now ",x)

z=5
print(y)
print_x(z,2)
print("after executing function now x is ",z)
print("after executing function now y is ",y)

#keyword arguments
print_x(x=5,times=0)

#var args parameter
def add_All(*number):
    result=0;
    for i in number:
        result+=number[i-1]
    print(result)

add_All(1,2,3,4,5,6)

def display_this(**phonebook):
    print(phonebook)
    for first_part,second_part in phonebook.items():
        print(first_part," - ",second_part)

display_this(john=123,abcd='efgh',ijkl=1.25)

#return statement
#doc string
#A string on the first logical line of a function is the docstring for that function
def max(x,y):
    '''this is a doc string for the function max. this function 
    checks two numbers finds which is maximum'''
    if(x>y):
        return x
    elif(x==y):
        return "Both are equal"
    else:
        return y

print(max(4,5))
print(max.__doc__)


