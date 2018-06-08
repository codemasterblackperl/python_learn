'''
A list is a data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list. This is easy to imagine if you can think of a shopping list where you have a list of items to buy, except that you probably have each item on a separate line in your shopping list whereas in Python you put commas in between them.

The list of items should be enclosed in square brackets so that Python understands that you are specifying a list. Once you have created a list, you can add, remove or search for items in the list. Since we can add and remove items, we say that a list is a mutable data type i.e. this type can be altered.
'''

shop_list=['apple','orange','mango','carret','onion']

print('I have ',len(shop_list),' items to purchase')

print('These items are: ')

for item in shop_list:
    print(item)

print('I have to buy rice also')

shop_list.append('rice')

shop_list.sort()

print('Now my shop list is \r\n',shop_list)

print('I will buy ',shop_list[0],' first')

item=shop_list[0]
del shop_list[0]

print('After buing ',item,' ,my shop list \r\n',shop_list)