# Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
    return True

# Get user input
number = int(input("Enter a number: "))

#Check if the number is prime
if is_prime(number):
     print(True,"the number is prime")
else:
     print(False, "the number is not prime")