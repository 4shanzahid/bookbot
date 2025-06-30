from stats import count_words , count_characters


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")
    character_count = count_characters(file_contents)
    print(character_count)


main()
