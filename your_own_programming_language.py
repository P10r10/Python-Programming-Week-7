from string import ascii_uppercase


def execute(command: list, output: list, variables: dict):
    if command[0] == "PRINT":
        output.append(variables.get(command[1]))
    if command[0] == "MOV":
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


def run(program: list):
    output = []
    variables = {ch: 0 for ch in ascii_uppercase}  # init variables
    commands = [line.split(" ") for line in program]
    i = 0
    while True:
        if commands[i][0] == "END":  # exit loop with END
            break
        if len(commands[i]) == 1:  # this is a tag
            variables[commands[i][0]] = i  # keeps current line in variables
        else:
            execute(commands[i], output, variables)
        i += 1
    return output


if __name__ == "__main__":
    # program1 = []
    # program1.append("MOV A 1")
    # program1.append("MOV B 2")
    # program1.append("PRINT A")
    # program1.append("PRINT B")
    # program1.append("ADD A B")
    # program1.append("PRINT A")
    # program1.append("END")
    # result = run(program1)
    # print(result)

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
    # program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)
