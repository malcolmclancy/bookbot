import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    chars_sorted_list = sort_dictionary_count(chars_dict)
    report = generate_report(book_path, num_words, chars_sorted_list)
    print(report)

def generate_report(book, words, characters):
    report = f"--- Begin report of {book} ---"
    report += f"\n{str(words)} words found in the document\n"
    for char in characters:
        report += f"\nThe character '{char["name"]}' was found {str(char["num"])} times"
    report += "\n--- End Report ---"
    return report

def sort_on(dict):
    return dict["num"]

def sort_dictionary_count(character_dictionary):
    clean = []
    for character in character_dictionary:
        if character.isalpha():
            char_count = {"name": character,
                "num": character_dictionary[f"{character}"]}
            clean.append(char_count)
    clean.sort(reverse=True, key=sort_on)
    return clean
    #print(list_letters)


def get_num_characters(text):
    word_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1
    return word_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
