import string


def separate_characters(my_string: str) -> tuple:
    a = ""
    b = ""
    c = ""
    for ch in my_string:
        if ch in string.ascii_letters:
            a += ch
        elif ch in string.punctuation:
            b += ch
        else:
            c += ch
    return (a, b, c)


parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])
print(parts[1])
print(parts[2])
