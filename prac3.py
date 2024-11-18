import numpy as np

my_list = np.array([1, 2, 3, 4, 5])
my_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=np.float64)
a3 = np.arange(8)
numbers = [1, 2 ,3 ,4, 5, 6, 7, 8]

print(numbers[2:6]) # Outputs: [3, 4, 5, 6]
print(numbers[:4]) # Outputs: [1, 2, 3, 4]
print(numbers[::2]) # Outputs: [1, 3, 5, 7]

print(my_list)print(my_array)
print(a3)