import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Correct! You guessed it.")
