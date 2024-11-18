from numpy import number

numbers = list(range(1, 51))
odd_numbers = [num for num in numbers if num % 2 != 0]
multiply_of_three = [num  for num in numbers if num % 3 == 0]
print(odd_numbers)
print(multiply_of_three)
