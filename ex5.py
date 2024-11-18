my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

#this line is tricky, try to get it exacly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

my_name = 'Z. Edudzi Shelter'
my_age = 20 # approximately
my_height = 66.5 #inches
my_weight = 132.3 # pounds
my_eyes = 'Brown' 
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"I'm {my_height} inches tall.")
print(f"I'm {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"I have {my_eyes} eyes and {my_hair} hair.")
print(f"My teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

#Python Weight converter
weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K":
 weight = weight*2.205
 unit = "Lbs."
elif unit== "L":
 weight = weight/2.205
 unit = "Kgs."
else:
 print(f"{unit} was not valid")
 
print(f"Your weight is {weight}{unit}")

#Rounding floating point
number = input("Entrer number: ")
v = 1.73333
print("The number rounded to 0 decimal place: ", round(v))
print("The number rounded to 1 decimal place: ", round(v, 1))
print("The number rounded to 2 decimal place: ", round(v, 2))
m=round(1.65432145789,6)
print(m)