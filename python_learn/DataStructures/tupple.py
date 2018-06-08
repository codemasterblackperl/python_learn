'''
Tuples are used to hold together multiple objects. Think of them as similar to lists, but without the extensive functionality that the list class gives you. One major feature of tuples is that they are immutable like strings i.e. you cannot modify tuples.

Tuples are defined by specifying items separated by commas within an optional pair of parentheses.

Tuples are usually used in cases where a statement or a user-defined function can safely assume that the collection of values (i.e. the tuple of values used) will not change.
'''
#paranthisis are optional
zoo=('monkey','tiger','lion')

print('Animals in zoo are: ',zoo)

newZoo='python','zebra',zoo

print('Animals in new zoo are: ',newZoo)

for animal in newZoo:
    print(animal)

print('last animal from zoo is : ',newZoo[2][2])

#to declare empty touple 
emptyTouple=()

#touple with single item is 
single_touple=(2,)