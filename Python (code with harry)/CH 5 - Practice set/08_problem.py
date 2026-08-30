#8. If languages of two friends are same; what will happen to the program in problem#
#6?
#6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
#value and use key as their names. Assume that the names are unique.
d = {}
a = input('enter name')
b = input('fav sub')
d.update({a:b})
a = input('enter name')
b = input('fav sub')
d.update({a:b})
a = input('enter name')
b = input('fav sub')
d.update({a:b})
a = input('enter name')
b = input('fav sub')
d.update({a:b})
print(d)
# values will be same but its ok because the key is unique so all will be printed