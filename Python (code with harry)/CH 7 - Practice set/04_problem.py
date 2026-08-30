#4. Write a program to find whether a given number is prime or not.
int1 = int(input ('enter the number: '))

c = 2
while c < int1 :
    if int1 % c == 0:
        print('the number is not prime')
        break

    c += 1

else:
   print('the number is prime number')    

