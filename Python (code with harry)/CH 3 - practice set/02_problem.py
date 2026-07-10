#2.rite a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace('<|Name|>' , 'Ambi').replace('<|Date|>' , '24th sep 2027'))