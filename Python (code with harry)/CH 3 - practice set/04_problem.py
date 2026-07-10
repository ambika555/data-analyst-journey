#4. Replace the double space from problem 3 with single spaces.
text  = 'python is  an amazing  programming language'
print(text.split())
cleaned_text = ' '.join(text.split())
print('before:' , text)
print('after: ' , cleaned_text)

#print(text.replace('  ' , ' '))