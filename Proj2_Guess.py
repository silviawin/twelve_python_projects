import random


def guess(x):
    random_number = random.randint( 1, x)
    guesses = 0
    while guesses != random_number:
        guesses = int(input(f"Guess a number between 1 and {x}: "))
        if guesses < random_number:
            print(" Too low, try again")
        elif guesses > random_number:
            print("Too high, try again")
    print(f"You guessed the number {random_number}")

guess(10)

