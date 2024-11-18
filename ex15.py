# import argv from sys module
from sys import argv

#get argv command line arguments (when running the file and assigning it to variables)
script, filename = argv

#Open the file (using the filename) and assign to a variable
txt = open(filename)

#print out the filename and print out the content of the opened file, using read()
print(f"Here's your file {filename}:")
print(txt.read())

#close txt file
txt.close()

#Print out instruction and ask for input using input()
print("Type the filename again agail:")
file_again = input("> ")

#Open the file (using the filename) and assign to a variable
txt_again = open(file_again)

#print out the content of the opened file, using read()
print(txt_again.read())

#Close file
txt_again.close()