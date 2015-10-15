__author__ = 'jdepaula'

import sys
import math


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    words = test.split(' ')

    result = ''

    for w in words:
        result += w[0].upper() + w[1:] + " "
    print result.rstrip()

test_cases.close()
