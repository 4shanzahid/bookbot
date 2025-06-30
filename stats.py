def count_words(file_contents):
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count


def count_characters(text):
    counts = {}
    for char in text.lower():
        if char == " ":
            continue
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
