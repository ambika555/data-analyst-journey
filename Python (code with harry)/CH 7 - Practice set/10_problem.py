# 10. Write a program to print multiplication table of n using for loops in reversed
# order.

inpu = int(input('enter the number: '))

# i = 10
# while(i>=1):
#     print(f'{inpu} * {i} = {inpu*i}')
#     i-=1

for i in range(10 , 0 , -1):
    print(f'{inpu} * {i} = {inpu*i}')