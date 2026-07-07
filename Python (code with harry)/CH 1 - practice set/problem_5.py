#5. Label the program written in problem 4 with comments. 

#import the required module
import os

#provide the path whose content u want to see
path = "/"

#use the listdir() function to get the contents from the path
contents = os.listdir(path)

#print the output
print("directory contents:" , contents)