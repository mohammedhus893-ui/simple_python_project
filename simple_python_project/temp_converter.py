"""
Converts temperatures between Celsius, Fahrenheit, and Kelvin.
"""


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def kelvin_to_celsius(k):
    return k - 273.15


def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Kelvin to Celsius")

    choice = input("Choose an option (1-4): ").strip()

    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid number.")
        return

    if choice == "1":
        print(f"Result: {celsius_to_fahrenheit(value):.2f} F")
    elif choice == "2":
        print(f"Result: {celsius_to_kelvin(value):.2f} K")
    elif choice == "3":
        print(f"Result: {fahrenheit_to_celsius(value):.2f} C")
    elif choice == "4":
        result = kelvin_to_celsius(value)
        if value < 0:
            print("Kelvin cannot be negative (absolute zero limit).")
        else:
            print(f"Result: {result:.2f} C")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
