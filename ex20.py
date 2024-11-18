# Import argv from sys module
from sys import argv

# Assigns command line arguments to variables
script, input_file = argv

# Define a print all function which prints the content of the file
def print_all(f):
    print(f.read())

# Rewinds our file to the original position or begining of the file
def rewind(f):
    f.seek(0)

# Print out a line number, followed by a line of the file (reading a single line at a time)
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open a file and assign it to a variable
current_file = open(input_file)

print("First let's print the whole file:\n")

# Print out the content of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Rewind the file to the first position
rewind(current_file)

print("Let's print three lines:")

# Set current line, print each line of the file with the line number
current_line = 1
print_a_line(current_line, current_file)

# Increase the current line number by 1
# Set current line, print each line of the file with the line number
current_line = current_line + 1
print_a_line(current_line, current_file)

# Increase the current line number by 1
# Set current line, print each line of the file with the line number
current_line = current_line + 1
print_a_line(current_line, current_file)