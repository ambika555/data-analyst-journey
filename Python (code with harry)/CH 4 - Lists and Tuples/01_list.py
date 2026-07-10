friends = ['Apple' , 'Orange', 5 , 345.06 , False ,'Akash', 'Rohan']
print(friends[0])
friends[0] = 'Grapes'#unlike strings lists are mutable

print(friends[0])
print(friends[1:4])
print(friends)

friends.append('Harry')
print(friends)

l1 = [ 1 , 34 , 62 , 2 , 6 , 11]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3 , 334) #insert 334 at index 3
print(l1)
l1.pop(3)
print(l1)
print(l1.pop(3))
print(l1)
