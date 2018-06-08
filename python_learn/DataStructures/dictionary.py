
# if you didnt use valid unique key then it will the last value for that key
# here it will display a:e@gmail.com
#address_book={
#    'a':'a@gmail.com',
#    'a':'b@gmail.com',
#    'a':'c@gmail.com',
#    'a':'d@gmail.com',
#    'a':'e@gmail.com',
#    }

#print(address_book)

address_book={
    'a':'a@gmail.com',
    'b':'b@gmail.com',
    'c':'c@gmail.com',
    'd':'d@gmail.com',
    'e':'e@gmail.com',
    }

print(address_book)

print('a\'s address is : ',address_book['a'])

del address_book['c']

print(address_book)

for name,address in address_book.items():
    print('Name: ',name,' and Address: ',address)

address_book['f']='f@gmail.com'

print(address_book)