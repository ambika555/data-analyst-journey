#4. Write a recursive function to calculate the sum of first n natural numbers.

'''
1 = 1
2 = 2+1
3 = 3+2+1
4 = 4+3+2+1
5 = 5+4+3+2+1

n = n + (n-1) + (n-2) + (n-3) + .....+1

'''
def SUM_of_num(n):
    if n == 1:
        return 1
    res = n + SUM_of_num(n-1)
    return res

NUM = int(input('enter the number: '))

print(F'SUM OF {NUM} NATURAL NUMBER IS: ', SUM_of_num(NUM))



