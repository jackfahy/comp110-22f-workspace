"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730482932"

word: str = input("Enter a 5 character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1: 
    print("Error: Character must be a single character.")
    exit()
instance: int = 0

print("Searching for " + character + " in " + word)
if character == word[0]:
    print(character + " found at index 0 ")
    instance = 1
if character == word[1]:
    print(character + " found at index 1 ")
    instance = instance + 1
if character == word[2]:
    print(character + " found at index 2 ")
    instance = instance + 1
if character == word[3]:
    print(character + " found at index 3 ")
    instance = instance + 1
if character == word[4]:
    print(character + " found at index 4 ")
    instance = instance + 1
if instance == 1:
    print(str(instance) + " instance of " + character + " found in " + word)
if instance > 1:
    print(str(instance) + " instances of " + character + " found in " + word)
if instance == 0:
    print("No instances of " + character + " found in " + word)