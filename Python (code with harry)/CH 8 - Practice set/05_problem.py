# #5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

#no space , 3stars ---line 1
#no space , 2stars ---line 2
#no space , 1 star ---line 3

def pattern(n):
    i = 0
    while (i < n):
        print('*' * (n-i) )
        i += 1

pattern(3)
