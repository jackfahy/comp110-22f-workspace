import code


def love(subject: str) -> str:
    """Given a subjet as a parameter, returns a loving string."""

    return f"I love you {subject}!"

subject: str = code

print(love(subject))

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""

    love_note: str = ""
    i: int = 0

    while i < n: 
        #todo: the body of loop
        love_note = love_note + love(to) + "\n"
        i += 1
    return love_note
