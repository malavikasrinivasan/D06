#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports

# Body


def uses_all(word, required_letters):
    word = set(word.lower())
    for letter in required_letters.lower():
        if letter not in word:
            return False
    return True


def count_uses_all(required_letters):
    count = 0
    with open("words.txt", "r") as f:
        file_contents = f.readlines()
    for word in file_contents:
        if uses_all(word.strip(), required_letters):
            count += 1
    print("Number of words using all of these letters ({}) is {}.".format(required_letters, count))

##############################################################################
def main():
    count_uses_all("aeiou")
    count_uses_all("aeiouy")

if __name__ == '__main__':
    main()
