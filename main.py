import string
from collections import defaultdict


def main():
    prepare_report("books/frankenstein.txt")


def count_words(str_input: str):
    return len(str_input.split())


def count_chars(str_input: str):
    result = defaultdict(int)
    for char in str_input:
        lower = char.lower()
        if lower in string.ascii_lowercase:
            result[lower] += 1
    return result


def sort_on(value: tuple[str, int]):
    return value[1]


def prepare_report(path: str):
    with open(path) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        char_dict = count_chars(file_contents)
        char_list: list[tuple[str, int]] = list(char_dict.items())
        char_list.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {path} ---")
        print(f"{num_words} words found in the document")
        for item in char_list:
            print(f"The '{item[0]}' character was found {item[1]} times")
        print("--- End Report ---")


if __name__ == "__main__":
    main()
