import random


def guess_number():
    number = random.choice(range(1, 101))
    dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
    guess = int(input("Guess a number from 1 to 100: "))

    attempts = 0
    if dificulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts != 0 and guess != number:
        if guess < number:
            attempts -= 1
            print("Too low.")
            print(f"You have {attempts} attempts remaining")
            guess = int(input("Make a guess: "))
        elif guess > number:
            attempts -= 1
            print("Too high.")
            print(f"You have {attempts} attempts remaining")
            guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You win! The number is {number}")
    if attempts == 0:
        print(f"Game Over! You lose! The number is {number}")


while input("Want to guess my number? ( y / n ): ") == 'y':
    guess_number()
