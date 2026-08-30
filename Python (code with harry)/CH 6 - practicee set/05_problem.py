#5. Write a program which finds out whether a given name is present in a list or not.

list = ['Ambika' , 'varsha' , 'vaishnavi' , 'puja']

input1 = input('enter ur name: ')

if input1 in list:
    print(f'your name {input1} is in the list')
else:
    print(f'your name is not in the list.')