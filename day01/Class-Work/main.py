# main.py
from math import area_of_rectangle, area_of_circle, area_of_triangle

# Rectangle
length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
print("Rectangle area:", area_of_rectangle(length, breadth))

# Circle
radius = float(input("Enter circle radius: "))
print("Circle area:", area_of_circle(radius))

# Triangle
base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
print("Triangle area:", area_of_triangle(base, height))
