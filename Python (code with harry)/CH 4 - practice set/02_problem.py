#2. Write a program to accept marks of 6 students and display them in a sorted
#manner.

marks = []
s1 = int(input('enter marks of student1'))
marks.append(s1)

s2 = int(input('enter marks of student2'))
marks.append(s2)

s3 = int(input('enter marks of student3'))
marks.append(s3)

s4 = int(input('enter marks of student4'))
marks.append(s4)

s5 = int(input('enter marks of student5'))
marks.append(s5)

s6 = int(input('enter marks of student6'))
marks.append(s6)
marks.sort()
print(marks)