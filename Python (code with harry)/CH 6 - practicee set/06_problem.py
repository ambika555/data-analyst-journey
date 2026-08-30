# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

mark = int(input('enter students mark: '))

if (90 <= mark < 100) :
    print('grade is EX')
elif (80 <= mark < 90) :
    print('grade is A')
elif (70 <= mark < 80) :
    print('grade is B')
elif (60 <= mark < 70) :
    print('grade is C')
elif ( 50 <= mark < 60):
    print('grade is D')
elif ( mark <= 50) :
    print('grade is F')
