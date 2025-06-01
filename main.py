from stats import get_word_count
from stats import get_character_count
from stats import dict_to_list
import sys
def get_book_text(filepath):
    file_string = ""
    with open(filepath) as f:
        file_string = f.read()
    return file_string

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        string = get_book_text(sys.argv[1])
        word_count = get_word_count(string)
        character_dict = get_character_count(string)
        character_list_sorted = dict_to_list(character_dict)
        print(f"============ BOOKBOT ============ \nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
        for i in range(len(character_list_sorted)):
            character = character_list_sorted[i]
            for char in character:
                if character["char"].isalpha() == True and char == "char":
                    print(f"{character["char"]}: {character["num"]}")
        print("============= END ===============")
main()