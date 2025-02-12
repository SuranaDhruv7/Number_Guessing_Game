import numpy as np
print("==== Welcome to the Number Guessing Game ====")
def number_guessing_game():
    min_value = 1
    max_value = 100
    print(f"Please think of a number between {min_value} and {max_value}. Can you Guess what is it.")

    number_to_guess = np.random.randint(min_value, max_value)
    attempts = 0

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
        
number_guessing_game()