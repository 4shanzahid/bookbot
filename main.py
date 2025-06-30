from stats import count_words, count_characters
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def sort_char_dict(character_count):
    character_items = list(character_count.items())
    character_items.sort(key=lambda item: item[1], reverse=True)
    return character_items


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    file_contents = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_count = count_words(file_contents)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_count = count_characters(file_contents)
    character_items = sort_char_dict(character_count)
    for char, count in character_items:
        print(f"{char}: {count}")

    print("============= END ===============")


main()
