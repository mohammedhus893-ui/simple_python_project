"""
Calculates the area of different geometric shapes:
circle, rectangle, and triangle.
"""
import math


def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(width, height):
    return width * height


def triangle_area(base, height):
    return 0.5 * base * height


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid number, please try again.")


def main():
    print("=== Area Calculator ===")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Choose a shape (1-3): ").strip()

    if choice == "1":
        radius = get_positive_number("Enter radius: ")
        print(f"Area = {circle_area(radius):.2f}")
    elif choice == "2":
        width = get_positive_number("Enter width: ")
        height = get_positive_number("Enter height: ")
        print(f"Area = {rectangle_area(width, height):.2f}")
    elif choice == "3":
        base = get_positive_number("Enter base: ")
        height = get_positive_number("Enter height: ")
        print(f"Area = {triangle_area(base, height):.2f}")
    else:
        print("Invalid choice. Please run the program again and choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
