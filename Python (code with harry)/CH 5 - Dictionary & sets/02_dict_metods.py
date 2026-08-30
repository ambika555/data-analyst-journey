marks = { 
    'hary': 100,
    'subham': 56,
    'rohan': 23 ,
     0:'Harry'
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({'hary': 78 , 'Renuka':77})
print(marks.items())

print(marks.get('hary'))
print(marks['hary'])

#print(marks.get('hary'))
#print(marks['hary'])

print(marks.get('hary2'))#it will give none
print(marks['hary2'])#but it will give error , so both are not same

