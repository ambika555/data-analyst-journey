#1. Write a program using functions to find greatest of three numbers.
# n1 = int(input('enter first number: '))
# n2 = int(input('enter second number: '))
# n3 = int(input('enter third number: '))

# def gn():
#     if (n1 > n2) and (n1 > n3):
#         print(f'{n1} is greater number.')
#     elif (n2 > n1) and (n2 > n3):
#         print(f'{n2} is greater number.')
#     elif (n3 > n1) and (n3 > n2):
#         print(f'{n3} is greater number.')

    
# gn()


#recursively trying
def greatest_of_the_two(x,y):
    if x > y :
        return x
    else:
        return y

def greatest_of_three(a,b,c):

    return greatest_of_the_two(a, greatest_of_the_two(b,c))

n1 = int(input('enter first number'))
n2 = int(input('enter second number'))
n3 = int(input('enter third number'))


a = greatest_of_three(n1 , n2 , n3)

print('greatest number is : ', a )







# 

