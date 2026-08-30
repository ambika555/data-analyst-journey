#1. Write a program to create a dictionary of Hindi words with values as their English
#translation. Provide user with an option to look it up!

Dictionary = {
    'काम' : 'work',
    'पिता' : 'father',
    'विचार' : 'Idea',
    'शायद' : 'Maybe'


}
key = input('Enter a key: ')
value = Dictionary[key]

print(f'the meaning of {key} is {value}')
