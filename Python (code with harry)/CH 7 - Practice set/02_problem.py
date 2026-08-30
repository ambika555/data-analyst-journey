# #2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# import re
# fruits = ['apple', 'banana', 'apricot', 'cherry', 'mango']
# selected_fruits = [fruit for fruit in fruits if re.match('a', fruit)]

# fruits = ['apple', 'banana', 'apricot', 'cherry', 'mango']
# selected_fruits = [fruit for fruit in fruits if fruit.startswith('a')]

l = ["Harry", "Soham", "Sachin", "Rahul"]

sel_l = [item for item in l if re.match('S', item)]
print(l)

sel_l = [items for items in l if items.startswith('S')]
print(l)





