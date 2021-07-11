import guess_art
import random


print("Welcome to the number guessing game!")
name = input("\nChoose a difficulty: 'easy' or 'hard': ")

# modified version
def easy_mode(user_number):
    tries = 10
    random_number = random.randint(0, 100)
    print(f"This is the random number {random_number}")
    if tries != 0:
        for i in range(tries):
            print(f"You have {tries} left! Be careful")
            print(f"This is the current user number:{user_number}")
            if user_number == random_number:
                return
            elif user_number < random_number:
                print("Number is too low, try again! ")
                new_number = int(input("Choose a new number "))
                tries -= 1
                user_number = new_number
            else:
                print("Number is too high")
                tries -= 1
                new_number = int(input("Choose a new number "))
    elif tries == 0:
        print("Your all out of tries please restart this game.")

def hard_mode(user_number):
    tries = 5
    random_number = random.randint(0, 100)
    print(random_number)
    if tries != 0:
        for i in range(tries):
            print(f"This is the random number {random_number}")
            print(f"You have {tries} left! Be careful")
            if user_number == random_number:
                return
            elif user_number < random_number:
                print("Number is too low, try again! ")
                new_number = int(input("Choose a new number "))
                tries -= 1
                user_number = new_number
            else:
                print("Number is too high")
                tries -= 1
                new_number2 = int(input("Choose a new number "))
                user_number = new_number2
    elif tries == 0:
        print("Your all out of tries please restart this game.")

if name == "easy":
    number_guessed = int(input("Guess a number! "))
    easy = easy_mode(number_guessed)
    print("You have won this game woo hoo!!!")

else:
    number_guessed = int(input("Guess a number! "))
    hard = hard_mode(number_guessed)
    print("You have won this game woo hoo!!!")