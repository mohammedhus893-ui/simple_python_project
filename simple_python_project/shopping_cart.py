"""
A simple shopping cart simulator.
Lets the user add items with prices and quantities,
then shows an itemized total.
"""


def main():
    cart = []
    print("=== Shopping Cart ===")
    print("Type 'done' as the item name when you're finished.\n")

    while True:
        name = input("Enter item name: ").strip()
        if name.lower() == "done":
            break

        try:
            price = float(input(f"Enter price for {name}: "))
            quantity = int(input(f"Enter quantity for {name}: "))
            if price < 0 or quantity <= 0:
                print("Price must be non-negative and quantity must be positive.\n")
                continue
            cart.append({"name": name, "price": price, "quantity": quantity})
        except ValueError:
            print("Invalid price or quantity, please try again.\n")

    if not cart:
        print("Your cart is empty.")
        return

    print("\n=== Receipt ===")
    total = 0.0
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} x{item['quantity']} = {subtotal:.2f}")

    print(f"\nTotal: {total:.2f}")


if __name__ == "__main__":
    main()
