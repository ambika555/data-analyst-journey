a = int(input('Enter your age:'))
#if elif else ladder

#if statement number 1
if(a%2 == 0):
    print('age is even')
#end of if statement 1

#if statement number 2
if(a >= 18):
    print('you are above te age of consent')

elif(a < 0):
    print('you are entering an invalid age')

elif(a == 0):
    print('you are entering zero which is invalid age')

else:
    print('you are below the age of consent')

print('End of program')
#end of if statement 2

