# PASSWORD GENERATOR
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return(f"Generate password: {password}")

# Generate a password of length 12
password = generate_password(12)
print(f"Generate password: {password}")