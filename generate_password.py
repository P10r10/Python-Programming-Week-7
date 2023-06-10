from string import ascii_lowercase
from random import choice


def generate_password(n: int) -> str:
    result = ""
    for i in range(n):
        result += choice(ascii_lowercase)
    return result


print(generate_password(8))
