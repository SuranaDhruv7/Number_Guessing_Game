import numpy as np
import time
print("==== Welcome to the Number Guessing Game ====")
def number_guessing_game():
    min_value = 1
    max_value = 100
    print(f"Please think of a number between {min_value} and {max_value}. Can you Guess what is it.")

    number_to_guess = np.random.randint(min_value, max_value)
    attempts = 0

    print("Choose the difficulty level: ")
    print("1. Easy (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (3 attempts)")
    difficulty = input("Enter your choice: ")
    if difficulty.isdigit():
        difficulty = int(difficulty)
    else:
        print("Invalid choice. Please enter a number.")
        return 
    if difficulty == 1:
        max_attempts = 10
        print("Game Loading...")
        time.sleep(3) 
    elif difficulty == 2:
        max_attempts = 5
        print("Game Loading...")
        time.sleep(3) 
    elif difficulty == 3:
        max_attempts = 3
        print("Game Loading...")
        time.sleep(3) 
    else:
        print("Invalid choice. Please try again.")
        return
    while True:
        guess = input("Enter your number: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        if max_attempts and attempts >= max_attempts:
            print(f"Sorry! You've run out of attempts. The number was {number_to_guess}.")
            break
number_guessing_game()