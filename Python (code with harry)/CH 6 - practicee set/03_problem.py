#3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

all_text = 'hey there , invest on this to make a lot of money'

list = ['Make a lot of money' , 'buy now' , 'subscribe this' , 'click this']

for item in list:
      if item.lower() in all_text.lower():
            print ('detected a spam')



#2 way
p1 = 'Make a lot of money'
p2 = 'buy now'
p3 = 'subscribe this'
p4 = 'click this'

message = input('enter ur comment: ')

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
      print('this comment is a spam')
else:
      print('this comment is not a spam')

