"""EX02 - One shot wordle - almost wordle"""
__author__ = "730482932"

secret: str = "python"

word: str = input(f"What is your {len(secret)}-letter guess? ")
while len(secret) != len(word):
    print(f"That was not {len(secret)} letters!")
    word: str = input("Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
wordle: str = ""


while i < len(secret):
    if  word[i] == secret[i]:
        wordle = wordle + GREEN_BOX 
    else:
        exists_elsewhere: bool = False
        alternate_index: int = 0
        while exists_elsewhere != True and alternate_index < len(secret):
            """Checking for letters that are in the word but in the wrong spot"""
            if secret[alternate_index] == word[i]:
                exists_elsewhere = True
            else:
                alternate_index +=1
        if exists_elsewhere is True:
            wordle += YELLOW_BOX
        else:
            wordle += WHITE_BOX
    i += 1
print(wordle)

if secret == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")






    