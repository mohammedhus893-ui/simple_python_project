"""
A simple command-line calculator.
Supports addition, subtraction, multiplication, and division,
with input validation and division-by-zero handling.
"""

def calculate(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError(f"Unknown operator '{op}'. Use one of + - * /")


def main():
    print("=== Simple Calculator ===")
    print("Operators available: + - * /")
    print("Type 'quit' at any time to exit.\n")

    while True:
        first = input("Enter first number: ").strip()
        if first.lower() == "quit":
            break

        op = input("Enter operator (+ - * /): ").strip()
        if op.lower() == "quit":
            break

        second = input("Enter second number: ").strip()
        if second.lower() == "quit":
            break

        try:
            a = float(first)
            b = float(second)
            result = calculate(a, op, b)
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Invalid input: {e}\n")
        except ZeroDivisionError as e:
            print(f"Math error: {e}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()
