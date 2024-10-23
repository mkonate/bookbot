def get_book(path):
    with open(path, 'r', newline='') as handle:
        return handle.read()

def count_words(some_text):
    return len(some_text.split())

def count_chars(some_text):
    ret = {}
    for char in some_text.lower():
        if char not in ret:
            ret[char] = 1
        else:
            ret[char] += 1
    return ret

def print_report(book_path):
    text = get_book(book_path)
    wc = count_words(text)
    char_count = count_chars(text)


    print(f"--- Begin report of {book_path} ---")
    print(f"{wc} words found in the document")
    print()

    for char, count in char_count.items():
        print(f"The '{char}' character was found {count} times")

    print("-- End report ---")
    



def main():
    book_path = 'books/frankenstein.txt'
    print_report(book_path)


main()

