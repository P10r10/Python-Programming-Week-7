import fractions


def fractionate(amount: int) -> list:
    return [fractions.Fraction(1, amount) for n in range(amount)]


for p in fractionate(3):
    print(p)
print()
print(fractionate(5))
