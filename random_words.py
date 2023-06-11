from random import sample


def words(n: int, beginning: str) -> list:
    start_with = []
    with open("words.txt") as fp:
        for word in fp:
            if word.startswith(beginning):
                start_with.append(word.strip())
    if len(start_with) < n:
        raise ValueError
    return sample(start_with, k=n)


word_list = words(3, "ca")
for word in word_list:
    print(word)
