def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 10, 3, 8])

print(f"{minimum}, {maximum}")