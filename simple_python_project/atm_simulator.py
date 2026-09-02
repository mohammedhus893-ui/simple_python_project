"""
A simple ATM simulator.
Supports checking balance, depositing, and withdrawing money,
with basic validation (no negative amounts, no overdrawing).
"""


def main():
    balance = 100.0  # starting balance
    print("=== ATM Simulator ===")
    print("Welcome! Your starting balance is 100.00\n")

    while True:
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            print(f"Your balance is: {balance:.2f}\n")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Deposit amount must be positive.\n")
                    continue
                balance += amount
                print(f"Deposited {amount:.2f}. New balance: {balance:.2f}\n")
            except ValueError:
                print("Invalid amount.\n")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.\n")
                    continue
                if amount > balance:
                    print("Insufficient funds.\n")
                    continue
                balance -= amount
                print(f"Withdrew {amount:.2f}. New balance: {balance:.2f}\n")
            except ValueError:
                print("Invalid amount.\n")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-4.\n")


if __name__ == "__main__":
    main()
