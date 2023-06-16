from difflib import get_close_matches as gcm


text = input("Write text: ")
misspelled = []
with open("wordlist.txt") as fp:
    words = [word.strip().upper() for word in fp]
    for word in text.split(" "):
        if word.upper() in words:
            print(f"{word} ", end="")
        else:
            print(f"*{word}* ", end="")
            misspelled.append(word)
    if misspelled:
        print("\nSuggestions:")
        for miss_w in misspelled:
            print(f"{miss_w}: ", end="")
            display = ""
            fp.seek(0)  # moves the file pointer to the start of the file again
            for sug_w in gcm(miss_w, fp):
                display += f"{sug_w.strip()}, "
            display = display[:-2]  # removes last ", "
            print(display)
