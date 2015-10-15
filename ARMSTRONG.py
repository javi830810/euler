__author__ = 'jdepaula'
import sys
import math

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.rstrip()

    result = 0
    for x in test:
        result += math.pow(int(x),len(test))
    print result == int(test)

test_cases.close()
