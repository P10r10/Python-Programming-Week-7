from string import ascii_uppercase


def execute(command: list, output: list, variables: dict):
    if command[0] == "PRINT":
        if command[1] in ascii_uppercase:
            output.append(variables.get(command[1]))
        else:
            output.append(int(command[1]))
    if command[0] == "MOV":
        if command[2] in ascii_uppercase:
            variables[command[1]] = variables[command[2]]
        else:
            variables[command[1]] = int(command[2])
    if command[0] == "ADD":
        if command[2] in ascii_uppercase:
            variables[command[1]] += variables.get(command[2])
        else:
            variables[command[1]] += int(command[2])
    if command[0] == "SUB":
        if command[2] in ascii_uppercase:
            variables[command[1]] -= variables.get(command[2])
        else:
            variables[command[1]] -= int(command[2])
    if command[0] == "MUL":
        if command[2] in ascii_uppercase:
            variables[command[1]] *= variables.get(command[2])
        else:
            variables[command[1]] *= int(command[2])
    if command[0] == "JUMP":
        variables["pc"] = variables[command[1]]
    if command[0] == "IF":
        if command[3] in ascii_uppercase:
            operator = variables[command[3]]
        else:
            operator = int(command[3])
        if command[2] == "==":
            if variables[command[1]] == operator:
                variables["pc"] = variables[command[5]]
        if command[2] == "!=":
            if variables[command[1]] != operator:
                variables["pc"] = variables[command[5]]
        if command[2] == "<":
            if variables[command[1]] < operator:
                variables["pc"] = variables[command[5]]
        if command[2] == "<=":
            if variables[command[1]] <= operator:
                variables["pc"] = variables[command[5]]
        if command[2] == ">":
            if variables[command[1]] > operator:
                variables["pc"] = variables[command[5]]
        if command[2] == ">=":
            if variables[command[1]] >= operator:
                variables["pc"] = variables[command[5]]


def run(program: list):
    if not program:  # program is empty
        return []
    output = []
    variables = {ch: 0 for ch in ascii_uppercase}  # init variables
    commands = [line.split(" ") for line in program]
    for pc in range(len(commands)):  # init tags with program counter value
        if len(commands[pc]) == 1 and commands[pc][0] != "END":
            variables[commands[pc][0][:-1]] = pc  # key has last ":" removed

    variables["pc"] = 0  # init program counter
    while True:
        if commands[variables["pc"]][0] == "END":  # exit loop with END
            break
        execute(commands[variables["pc"]], output, variables)
        variables["pc"] += 1
        if variables["pc"] >= len(commands):
            break  # exit when program hits last line
    return output


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

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    program3 = []  # factorial
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

    program4 = []  # prime numbers
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)

    program5 = []  # empty program test
    result = run(program5)
    print(result)
