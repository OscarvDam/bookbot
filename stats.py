def get_num_words(fileText):
    return len(fileText.split())

def get_letter_count(fileText):
    words = fileText.lower().split()
    countletters = {}
    for word in words:
        letters = word[::]
        for letter in letters:
            if letter in countletters:
                countletters[letter] += 1
            else:
                countletters[letter] = 1
    return countletters

def sort_on(items):
    return items["count"]

def get_ordered_dictonary(dictonary):
    char_count = []
    for key in dictonary:
        setCharCount = {
                "char": key,
                "count": dictonary[key]
                }
        char_count.append(setCharCount)
    char_count.sort(reverse=True, key=sort_on)
    return char_count
