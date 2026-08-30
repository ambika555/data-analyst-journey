# 7. Write a python function to remove a given word from a list and strip it at the same
# time from all the words

def func(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(' '))
    return n
list = ['apple' , 'mango  ', ' banana ' , 'kiwi  ']

a = func(list , 'apple')
print(a)
