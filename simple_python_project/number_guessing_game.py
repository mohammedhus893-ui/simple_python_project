"""
A number guessing game. The computer picks a random number
between 1 and 100, and the player tries to guess it with hints.
"""
import random


def main():
    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess_input = input("Your guess: ").strip()
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()
