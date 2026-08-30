#2. Write a python program using function to convert Celsius to Fahrenheit.
#°F = 9/5°C + 32

def C_to_F(Celcius) :
    Fahrenheit = (9/5) * Celcius + 32
    return Fahrenheit

C = int(input('enter the celcius value: '))

print('the fahrenheit value is', C_to_F(C))

    
    
