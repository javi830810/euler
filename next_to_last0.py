__author__ = 'jdepaula'
import sys
import math

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.rstrip()

    sentence = test.split(' ')
    print sentence[len(sentence)-2]

test_cases.close()
