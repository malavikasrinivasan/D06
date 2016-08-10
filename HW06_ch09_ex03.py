#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
from string import ascii_lowercase

# Body


def avoids(word, forbidden_letters):
    """ return True if word NOT forbidden"""
    forbidden_letters = set(forbidden_letters)  # Set gets a set of unique values from the string/list
    for letter in word:
        if letter in forbidden_letters:
            return False
    return True


def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    forbidden_letters = input("Enter the forbidden letters one at a time - ")
    with open("words.txt", "r") as f:
        file_contents = f.readlines()
    not_forbidden = 0
    for word in file_contents:
        if avoids(word.strip(), forbidden_letters):
            not_forbidden += 1
    print("Number of words without these forbidden letters ({}) is {}.".format(forbidden_letters, not_forbidden))


def forbidden_param(forbidden_letters):
    """ return count of words NOT forbidden by param"""
    ...
    with open("words.txt", "r") as f:
        file_contents = f.readlines()
    not_forbidden = 0
    for word in file_contents:
        if avoids(word.strip(), forbidden_letters):
            not_forbidden += 1
    print("Number of words without these forbidden letters ({}) is {}.".format(forbidden_letters, not_forbidden))
    return not_forbidden


def find_five():

    # Find the number of words each letter appears in
    # TODO : Finish this. Too sleepy to think
    alphabet_word_count_list = []
    for letter in ascii_lowercase:
        word_count = forbidden_param(letter)

##############################################################################
def main():
    ...
    # Your final submission should only call five_five
    forbidden_prompt()

if __name__ == '__main__':
    main()
