def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

import sys
from stats import get_num_words
from stats import get_num_letters
from stats import sort_char_count

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
#    path = "/home/bingobeawr/bookbot/books/frankenstein.txt"
#    text = get_book_text(path)
#    word_count = get_num_words(text)
#    print(f"Found {word_count} total words")
#    character_counts = get_num_letters(text)
#    for char, count in character_counts.items():
#            print(f"'{char}': {count}")
    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_counts = get_num_letters(text)
    sorted_chars = sort_char_count(char_counts)

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")

    print("============= END ===============")

main()
