# Predicting Game!
import random
import itertools

target = random.randint(1, 100)
guess = None
guesses = 0
play_again = "Yes"

while play_again == "Yes":
    while guess != target:
        guess = int(input("Guess a number between 1 and 100: "))
            
        if guess < target:
            print("Too low!")
            guesses = guesses + 1
            print(f"Number of attempt {guesses}")
        elif guess > target:
            print("Too high!")
            guesses = guesses + 1
            print(f"Number of attempt {guesses}")
        else:
            print(f"Correct! you have attempted {guesses} misses before getting it correct.")                
    play_again =input("Do you want to play again?\n(Yes or No) ")
    if play_again == "Yes":
        target = random.randint(1, 100)
        guesses = 0
        print("Alright, let's play again.")
        print("I have a new guess mind guess between 1 and 100")
    elif play_again == "No":
        print("Sorry to see you leave soon.\nWould you like to rate this game 5 star?\nPress 1 to continue or 9 to cancel")
        print("""1.Yes\n9. No\nEnter to continue:""", end='')
        continue_rating = int(input(""))
        if continue_rating == 1:
            print("Enter from 1 to 5:", end='')
            rate = int(input(""))        
            if rate == 1:
                print("🥵 Sorry to  hear you are very unsatisfied with our game")
            elif rate == 2:
                print("🤒 Sorry to hear you are unsatisfied with our game.")
            elif rate == 3:
                print("😑 Thank you for your feed back.")
            elif rate == 4:
                print("😆 Thank you for being satisfied with our game.")
            elif rate == 5:
                print("🤩 We are glad that you are very satified with our game.")
            else:
                print("Invalid input received.")
        elif continue_rating == "9":
            print("Goodbye!")
        else:
            print("Invalid Input received")
    else:
        print("nvalid input received")
