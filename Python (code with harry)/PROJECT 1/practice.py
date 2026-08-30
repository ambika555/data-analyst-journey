'''
rules 

gun beats snake
snake beats water
water beats gun

'''
import random

youDict = { 'snake' : 1 , 'gun' : 0 , 'water' : -1 }
reverseDict = { 1 : 'snake' , 0 : 'gun' , -1 : 'water'}

# print(youDict['snake'])
# print(reverseDict[1])

def get_user_move():
    choice = input('enter your choice: ')
    return youDict[choice]

move = get_user_move()


def get_computer_move():
    a = random.choice([1, 0 , -1])
    return a

computer = get_computer_move()

print(f'computer chooses {reverseDict[computer]}')

# for i in range(10):
#     print(get_computer_move())



# you	computer	you - computer	winner
# 1	1		        0            tie
# 1	0		        1            you loose
# 1	-1		        2            you win
# 0	1		        -1           you win
# 0	0		        0            tie
# 0	-1		        1            you loose
# -1	1		        -2           you loose
# -1	0		        -1           you win
# -1	-1		         0            tie



def decide_winner(move , computer ):
    if(move - computer == 2) or (move - computer == -1):
        print('you win!! , computer looses!')
    elif(move - computer == 1) or (move - computer == -2):
        print('computer wins!! , you loose!')
    else:
        print('draw')



decide_winner(move , computer)




