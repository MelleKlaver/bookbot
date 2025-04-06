import os
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from command-line argument
path = sys.argv[1]


from stats import get_num_words, lettercounter, sort_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
text = get_book_text(path)
word_count = get_num_words(text)
sorted_chars = sort_characters(text)

def print_report(filepath, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha(): 
            print(f"{char}: {count}")
    
    print("============= END ===============")

print_report(path, word_count, sorted_chars)