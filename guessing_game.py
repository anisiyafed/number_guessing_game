
print("Welcome to number guessing game!")
print("I am thinking of a number between 1 and 100. Take a guess:")

import random
number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess: ")
    guess = int(guess)
    attempts = attempts + 1

    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < number_to_guess: print("Too low. Try again!")
    else: print("Too high. Try again!")
