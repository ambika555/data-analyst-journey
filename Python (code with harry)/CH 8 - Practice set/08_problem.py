#8. Write a python function to print multiplication table of a given number.

def mul(n):
    i = 1
    while(i<= 10):
        print(f'{n} * {i} = {n*i}')
        i+= 1

n = int(input('enter your number: '))

mul(n)


