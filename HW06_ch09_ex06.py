#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body


def is_abecedarian(word):
    """ Returns True if the letters in word appear in alphabetical order
        TODO : Handle presence of special characters - Find a way to strip string off of special characters/numbers
    """
    word = word.lower()  # Converting word to lower case to use ascii values for comparison
    word_len = len(word)
    if word_len == 1:
        return True
    for i in range(0, word_len-1):
        if ord(word[i]) > ord(word[i+1]):  # Checking if the next letter's ASCII 
            return False
    return True

def count_abecedarian():
    abecedarian_word_count = 0
    with open("words.txt", "r") as f:
        file_contents = f.readlines()
    for word in file_contents:
        if is_abecedarian(word.strip()):
            abecedarian_word_count += 1
    print("Number of abecedarian words in the file are {}".format(abecedarian_word_count))


##############################################################################
def main():
    count_abecedarian()

if __name__ == '__main__':
    main()
