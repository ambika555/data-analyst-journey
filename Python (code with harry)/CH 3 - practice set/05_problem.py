#5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry, this python course is nice. Thanks!"

letter_escape_sequence = 'Dear\\ Harry,\nthis python course\tis nice. \'thanks\''
print(letter_escape_sequence)#strings are immutable it means that you cannot change them by running functions on them