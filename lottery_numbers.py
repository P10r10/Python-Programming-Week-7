from random import sample


def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    return sample(list(range(lower, upper + 1)), amount)


for number in lottery_numbers(7, 1, 40):
    print(number)
