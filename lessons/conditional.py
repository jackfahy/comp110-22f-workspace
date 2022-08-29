"""An example of conditional (if-else) statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = input("What is your guess?")

if guess == SECRET:
    print("You guessed correctly!!")
    print("Have a wonderful day!")
else:
    print("Sorry, you guessed incorrectly :(")
    print("Try running the program again.")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print ("You guessed too low!")

print("Game over.")