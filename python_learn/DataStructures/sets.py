bri={'india','russia','japan'}

print('Is india in bri: ', 'india' in bri)
print('Is usa in bri: ','usa' in bri)

bric=bri.copy()
bric.add('china')
print('Is china in bri: ','china' in bri)
print('Is china in bric: ','china' in bric)

print('Is bric superset of bri: ',bric.issuperset(bri))

bri.remove('russia')

print('Intersection of bri and bric: ',bri&bric)

#is same as above

print('Intersection of bri and bric: ',bri.intersection(bric))


#Remember that if you want to make a copy of a list or such kinds of sequences or 
#complex objects (not simple objects such as integers), 
#then you have to use the slicing operation to make a copy. 
#If you just assign the variable name to another name, both of them will ''refer'' to the same object 
#and this could be trouble if you are not careful.

# This is a string object
name = 'Ajit'

if name.startswith('A'):
    print('Yes, the string starts with "A"')

if 't' in name:
    print('Yes, it contains the string "t"')

if name.find('ji') != -1:
    print('Yes, it contains the string "ji"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))