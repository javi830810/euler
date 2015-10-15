__author__ = 'jdepaula'
import sys

from itertools import permutations
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.rstrip()
    s1, s2 = test.split(',')

    if s1 in s2+s2:
        print True
    else:
        print False

test_cases.close()
