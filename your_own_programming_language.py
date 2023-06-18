def unpack(program: list) -> list[list]:
    """
    INPUT: list of strings containing the program
    OUTPUT: list of lists with instructions and respective operands
    """
    return [line.split(" ") for line in program]


def run(program: list):
    for command in unpack(program):
        print(command)


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)
