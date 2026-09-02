"""
Converts weights between kilograms, grams, and pounds.
"""

KG_TO_LB = 2.20462
LB_TO_KG = 1 / KG_TO_LB


def main():
    print("=== Weight Converter ===")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Kilograms to Grams")
    print("4. Grams to Kilograms")

    choice = input("Choose an option (1-4): ").strip()

    try:
        value = float(input("Enter the weight value: "))
        if value < 0:
            print("Weight cannot be negative.")
            return
    except ValueError:
        print("Invalid number.")
        return

    if choice == "1":
        print(f"Result: {value * KG_TO_LB:.2f} lb")
    elif choice == "2":
        print(f"Result: {value * LB_TO_KG:.2f} kg")
    elif choice == "3":
        print(f"Result: {value * 1000:.2f} g")
    elif choice == "4":
        print(f"Result: {value / 1000:.4f} kg")
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
