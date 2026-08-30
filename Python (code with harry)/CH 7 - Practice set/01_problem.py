#1. Write a program to print multiplication table of a given number using for loop.

inp = int(input('enter the number : '))

i = 1
while(i<11):
    print(f'{inp} * {i} = {inp * i}')
    i += 1

for i in range(1, 11):
     print(f'{inp} * {i} = {inp * i}')

