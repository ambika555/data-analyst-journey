#6. Write a python function which converts inches to cms.
# Centimeters=Inches×2.54

def In_to_cm(inch):
    Centimeters = inch * 2.54 
    return Centimeters

n = int(input('enter the number in inches: '))

a = In_to_cm(n)

print('the number in centimeters is : ' , a)



    

