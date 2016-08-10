#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body


def has_no_e(word):
    if word.find('e') == -1:
        return True
    else:
        return False


def print_no_e(filename):
    with open(filename, "r") as f:
        words = f.readlines()
    total_words = len(words)
    words_without_e = 0
    for word in words:
        if has_no_e(word.strip()):
            print(word.strip())
            words_without_e += 1
    print("{:.2%} of all the words in the file have no e".format(words_without_e/total_words))


##############################################################################
def main():
    print_no_e("words.txt") 

if __name__ == '__main__':
    main()
