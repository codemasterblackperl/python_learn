
age=29
name='Ajit'

print("{0} was {1} year old when he printed this".format(name,age))
print(name+" was "+str(age)+' year old when he tried it again with different print method')

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {program}'.format(name='Ajit H', program='string format in python program'))

#python basically adds a new line for each print so to prevent that add end='' or end=' ' in print
print('a',end=' ')
print('b',end='\r\n')

#raw string
print(r'this is raw string \n')