from stats import get_num_words
from stats import get_letter_count
from stats import get_ordered_dictonary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1] 
    print("========= BOOKBOT =========")
    print(f"Analyzing book found at {path}")
    fileText = get_book_text(path)
    num_words = get_num_words(fileText)
    num_letters = get_letter_count(fileText)
    print("------------- Word Count -------------")
    print(f"Found {num_words} total words")
    ordered_dictonary = get_ordered_dictonary(num_letters)
    print("----------- Character Count -----------")
    for dictonary in ordered_dictonary:
        dicto = dict(dictonary)
        print(f"{dicto["char"]}: {dicto["count"]}")
main()

