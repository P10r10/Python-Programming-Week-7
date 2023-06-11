from random import choice


def roll(die: str) -> int:
    if die == "A":
        return int(choice("333336"))
    if die == "B":
        return int(choice("222555"))
    if die == "C":
        return int(choice("144444"))


def play(die1: str, die2: str, times: int) -> tuple:
    win = 0
    lose = 0
    tie = 0
    for _ in range(times):
        die1_roll = roll(die1)
        die2_roll = roll(die2)
        if die1_roll > die2_roll:
            win += 1
        elif die1_roll < die2_roll:
            lose += 1
        else:
            tie += 1
    return (win, lose, tie)


for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")

result = play("A", "C", 1000)
print(result)
result = play("B", "B", 1000)
print(result)
