def count_words(file_contents):
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count +=1
    return word_count
