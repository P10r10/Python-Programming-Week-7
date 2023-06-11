from string import ascii_lowercase, digits
from random import choice, randint, sample, seed


def generate_strong_password(n: int, has_num: bool, has_sp: bool) -> str:
    result = ""
    if not has_num and not has_sp:
        for i in range(n):
            result += choice(ascii_lowercase)
        return result
    elif not has_num and has_sp:
        try:
            nb_special = randint(1, n - 1)
        except:
            nb_special = 0
        for i in range(nb_special):
            result += choice("!?=+-()#")
        for i in range(n - nb_special):
            result += choice(ascii_lowercase)
        return "".join(sample(result, k=len(result)))  # converts list to str
    elif has_num and not has_sp:
        try:
            nb_nums = randint(1, n - 1)
        except:
            nb_nums = 0
        for i in range(nb_nums):
            result += choice(digits)
        for i in range(n - nb_nums):
            result += choice(ascii_lowercase)
        return "".join(sample(result, k=len(result)))  # converts list to str
    else:
        try:
            nb_nums = randint(1, n - 2)
        except:
            nb_nums = 1
        try:
            nb_special = randint(1, n - 2 - nb_nums)
        except:
            nb_special = 1
        for i in range(nb_nums):
            result += choice(digits)
        for i in range(nb_special):
            result += choice("!?=+-()#")
        for i in range(n - nb_nums - nb_special):
            result += choice(ascii_lowercase)
        return "".join(sample(result, k=len(result)))  # converts list to str


print(generate_strong_password(8, False, False))
print(generate_strong_password(8, False, True))
print(generate_strong_password(8, True, False))
print(generate_strong_password(8, True, True))
print(generate_strong_password(5, True, True))
