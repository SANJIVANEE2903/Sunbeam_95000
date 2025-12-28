# print("Hello World!")

# main.py

from geometry import area, perimeter
from arithmetic import add, subtract

def main():
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    # Geometry calculations
    rect_area = area(length, breadth)
    rect_perimeter = perimeter(length, breadth)

    # Arithmetic calculations
    addition = add(length, breadth)
    subtraction = subtract(length, breadth)

    print("\n--- Results ---")
    print("Area:", rect_area)
    print("Perimeter:", rect_perimeter)
    print("Addition:", addition)
    print("Subtraction:", subtraction)

if __name__ == "__main__":
    main()
