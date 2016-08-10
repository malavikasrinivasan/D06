#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoey()
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: aloe ha
#       2: cooch fool
#       3: halloo lace
##############################################################################
# Imports
from random import randint
# Body


def uses_only(word, required_letters):
    required_letters = set(required_letters)
    for letter in word.lower():
        if letter not in required_letters:
            return False
    return True


def find_words_with_all(required_letters):
    with open("words.txt", "r") as f:
        file_contents = f.readlines()
    words_using_all = []
    for word in file_contents:
        if uses_only(word.strip(), required_letters):
            words_using_all.append(word.strip())
    # print("Words using all of these ({}) letters are - ".format(required_letters))
    # print(words_using_all)
    return words_using_all


def make_sentences(sentence_count, required_letters):
    """ Makes n sentences with words which only have the letters in required 
        letters from words.txt """
    valid_words = find_words_with_all(required_letters)
    for n in range(0,sentence_count):
        sentence = valid_words[randint(0,len(valid_words))] + " " + valid_words[randint(0, len(valid_words))]
        print(sentence)


##############################################################################
def main():
    make_sentences(3, "acefhlo")

if __name__ == '__main__':
    main()
