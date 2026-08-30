'''
1 for snake
-1 for water
0 for gun

'''
import random 
import sys

    

# computer = -1
youstr = input('enter your choice: ')
youDict = {'s' : 1 , 'w':-1 , 'g':0 }
reverseDict = { 1: 'Snake' , -1 :'water' , 0:'Gun'}
you = youDict[youstr]

def computer_move():
    return random.choice([1, -1, 0])

computer = computer_move()

#by now u have two numbers (variables ), you and computer
print(f'you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}')

computer_move()

if(computer == -1 and you == 1 ):
    print('you win!')

elif(computer == -1 and you == 0 ):
    print('you lose')

elif(computer == -1 and you == -1):
    print('TIE')

elif(computer == 1 and you == -1):
    print('you lose')
elif(computer == 1 and you == 0):
    print('you win')
elif(computer == 1 and you == 1):
    print('TIE')
elif(computer == 0 and you == 0):
    print('TIE')
elif(computer == 0 and you == -1):
    print('you win')
elif(computer == 0 and you == 1):
    print('you lose')

else:
    print('something went wrong')







    

