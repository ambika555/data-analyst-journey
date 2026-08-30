#6. Write a program to calculate the factorial of a given number using for loop.
int1 = int(input('enter a number: '))

mul = 1 
i = 1

while(i<= int1):
    mul = mul* i
    i += 1

print(f'the factorial of number {int1} is   ',mul)



