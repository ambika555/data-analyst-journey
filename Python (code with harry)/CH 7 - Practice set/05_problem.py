#5. Write a program to find the sum of first n natural numbers using while loop.

int1 = int(input('enter the number: '))

sum = 0
i = 1

while(i<= int1):
    sum = sum + i
    i += 1
print('sum is' , sum)

