# Positional Arguments
def multiply(a, b):
    return a * b

result = multiply (3, 5) #Positional arguments
print(result)

# Keyword Arguments
def greet(name, age):
    print("Hello,",name, "You are", age, "years old.")

greet(age=30, name="Alice") # Output

# Default Arguments
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice")) # Uses default message
print(greet("Bob", "Hi")) # Custom message

# Variable-Length Arguments:
 # *args: 
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3, 4))

# Variable-Length Arguments:
 #  **kwargs:
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Alice", age=30, city="New York")

