"""
Calculates the hypotenuse of a right triangle
using the Pythagorean theorem: c = sqrt(a^2 + b^2)
"""
import math


def main():
    print("=== Hypotenuse Calculator ===")
    try:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        if a <= 0 or b <= 0:
            print("Side lengths must be positive numbers.")
            return
        c = math.sqrt(a ** 2 + b ** 2)
        print(f"The hypotenuse is: {c:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
