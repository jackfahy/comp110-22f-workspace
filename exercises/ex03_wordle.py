"""The real wordle!"""
__author__ = "730482932"


def contains_char(word: str, letter: str) -> bool:
    """Function is checking the string and a single character"""
    assert len(letter) == 1
    i: int = 0

    while i < len(word):
        if word[i] == letter:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Checking to see if letters match or not using emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    answer: str = ""

    while i < len(secret):
        if guess[i] == secret[i]:
            answer += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            answer += YELLOW_BOX
        else:
            answer += WHITE_BOX
        i += 1
    return answer


def input_guess(length: int) -> str:
    """Letting user input a number that will be how many characters are in the word"""
    user_input: str = input(f"Enter a {length} character word: ")
    while len(user_input) != length:
        user_input = (f"That was not {length} chars! Try again: ")
    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    i: int = 1
    user_guess: str = ""

    while i < 7 and user_guess != secret_word:
        """When the amount of turns are less than 7 and user hasn't guessed secret word """
        print(f"=== Turn {i}/6 ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {i}/6 turns!")
        else:
            i += 1
    if i == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()