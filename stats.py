def get_wordcount(book):
    words = book.split()
    return len(words)

def get_charactercount(book):
    string = book.lower()
    character = {}

    for ch in string:
        if ch in character:
            character[ch] += 1
        else:
            character[ch] = 1
    return character

def sort_on(d):
    return d["num"]

def sorted_list(num_chars_dict):
    sorted = []
    for ch in num_chars_dict:
        sorted.append({"char": ch, "num": num_chars_dict[ch]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted