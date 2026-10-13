# ==========================================
# Number Guessing Game
# ==========================================

import random


# Function to play one round of the game
def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Count the number of valid guesses
    attempts = 0

    print("\n================================")
    print("       NUMBER GUESSING GAME")
    print("================================")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the correct number!")

    # Repeat until the user guesses correctly
    while True:
        try:
            # Get the user's guess
            guess = int(input("\nEnter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            attempts += 1
            # Compare the guess with the secret number

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print("\nCongratulations! You guessed it!")
                print(f"The correct number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

def main():
    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if choice != "yes":
            print("\nThank you for playing!")
            print("Good luck with your CodeOrbit internship!")
            break
if __name__ == "__main__":
    main()
