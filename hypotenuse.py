from math import sqrt


def hypotenuse(leg1: float, leg2: float) -> float:
    return sqrt(leg1**2 + leg2**2)


print(hypotenuse(3, 4))  # 5.0
print(hypotenuse(5, 12))  # 13.0
print(hypotenuse(1, 1))  # 1.4142135623730951
