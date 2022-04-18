# Number guessing game
import random
print("Welcome to the number guessing game!\n")
print("I'm thinking of a number between 1 to 100.\n")
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
is_game_end = False

def guess(my_guess,number,attempt):
    if my_guess>number:
        print("Your guess is too high!")
        return attempt-1

    elif my_guess<number:
        print("Your guess is too low!")
        return attempt-1

    else:
        print(f"You guess the correct number successfully! The number is {number}.")

def difficulty():
    level=input("Choose a dificulty level. Type 'easy' or 'hard':")
    
    if level=="easy":
        return EASY_LEVEL_ATTEMPTS
    elif level=="hard": 
        return HARD_LEVEL_ATTEMPTS
    else:
        return "Enter a valid input."


number= random.randint(1,100)
print(number)
attempt=difficulty()
my_guess=0
while my_guess!=number:

    print(f"You have {attempt} attempts remaining to guess the number.")
    my_guess =int(input("Make a guess:\n"))
    attempt=guess(my_guess,number,attempt)
    if attempt==0:
        print("You have exceeded the limit of guessing chances.")
    elif guess!= number:
        print("Guess again.")