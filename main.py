def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    nums_word = word_count(text)
    nums_of_letters = num_of_char(text)
    mapped = key_map(nums_of_letters)
    

    print_report(book_path, nums_word, mapped)


def get_book_path(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def num_of_char(text):
    char_map = {}
    lower_text = text.lower()
    
    for char in lower_text:
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1
    
    return char_map

def key_map(char_map):
    def sort_on(dict):
        return dict['num']
    char_list = [{'char' : key, 'num' : value} for key, value in char_map.items() if key.isalpha()]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

def print_report(text, letter, char_map):

    print(f"--- Begin report of {text} ---")
    print(f"{letter} words found in the document")
    
    for item in char_map:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

main()