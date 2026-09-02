"""
Calculates compound interest given principal, annual rate,
number of times interest is compounded per year, and time in years.

Formula: A = P * (1 + r/n)^(n*t)
"""


def compound_interest(principal, rate, times_per_year, years):
    return principal * (1 + rate / times_per_year) ** (times_per_year * years)


def main():
    print("=== Compound Interest Calculator ===")
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (as a %, e.g. 5 for 5%): ")) / 100
        times_per_year = int(input("Enter number of times compounded per year: "))
        years = float(input("Enter number of years: "))

        if principal < 0 or rate < 0 or times_per_year <= 0 or years < 0:
            print("Please enter valid positive values.")
            return

        final_amount = compound_interest(principal, rate, times_per_year, years)
        interest_earned = final_amount - principal

        print(f"Final amount: {final_amount:.2f}")
        print(f"Interest earned: {interest_earned:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
