#3.Write a program to detect double space in a string.
s = 'geeks  for  geeks'
print( s.find('  '))
res = s.count('  ') > 0
print(s.count('  '))
print(res)