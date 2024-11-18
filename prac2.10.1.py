import math

def calculate_area(width, height):
    return width*height

def calculate_area_of_triangle(base, height):
    return 1/2*base*height

def calculate_area_of_circle(r):
    return math.pi*r**2

# Test the function with different inputs
area1 = calculate_area(5, 10)
area2 = calculate_area(3, 7)
area3 = calculate_area_of_triangle(10, 7)
area4 = calculate_area_of_circle(7)
Pi=math.pi

print(f"Area of rectangle 1: {area1}")
print(f"Area of rectangle 2: {area2}")
print(f"Area of triangle 1: {area3}")
print(f"Area of circle 1: {area4}")
print(Pi)

