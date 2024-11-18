#FUNCTION AND VARIABLES

# Define a function cheese_and_crackers with 2 parameters
# Inside the function: Use arguments within print statements
def cheese_and_crackers(cheese_count, boxes_of_crackers): 
    print(f"You have {cheese_count} cheeses! ")
    print(f"You have {boxes_of_crackers} boxes of crackers! ")
    print("Man that's enough for a party! ")
    print("Get a blanket.\n")

# call our function with numbers as arguments
print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

# Defined two variables and assigns them with numbers
print("OR, can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

# Call the function with variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Call our function and pass calculation as argument
print("We can even do inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

#Call our function and passes calculation (with variable and numbers) as argument to it
print("And We can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

