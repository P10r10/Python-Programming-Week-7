from string import (
    ascii_lowercase, ascii_uppercase, ascii_letters, digits, whitespace
)


def change_case(orig_string: str) -> str:
    result = ""
    for letter in orig_string:
        if letter in ascii_lowercase:
            result += letter.upper()
        elif letter in ascii_uppercase:
            result += letter.lower()
        else:
            result += letter
    return result


def split_in_half(orig_string: str) -> tuple:
    size = len(orig_string)
    return orig_string[:size // 2], orig_string[size // 2:]


def remove_special_characters(orig_string: str) -> str:
    result = ""
    for letter in orig_string:
        if letter in ascii_letters or letter in digits or letter in whitespace:
            result += letter
    return result


if __name__ == "__main__":
    print(change_case("Well hello there!"))
    print(split_in_half("Well hello there!"))
    print(
        remove_special_characters("This is a test, lets see how it goes!!!11!")
    )
