# Temperature converter

# Ask for conversion type
conversion_type = input("""To convert from:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
 enter 1 or 2 respectively
>""")

# Perform conversion
if conversion_type == "1":
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius *9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")
elif conversion_type == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celsius}°C")
else:
    print("Invalid input. Please enter 1 or 2.")