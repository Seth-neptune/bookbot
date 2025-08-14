from stats import (
    get_wordcount,
    get_charactercount,
    sorted_list,
)
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read() 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_wordcount(book)
    character_count = get_charactercount(book)
    character_list = sorted_list(character_count)
    print_report(book_path, num_words, character_list)
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============== END ==============")




main()