__author__ = 'jdepaula'
import sys
import math

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()

    longest_word = ''
    for word in test.split(' '):
        if len(word) > len(longest_word):
            longest_word = word
    print longest_word

test_cases.close()
