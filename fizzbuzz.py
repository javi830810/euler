__author__ = 'jdepaula'

import sys
import math


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    x, y, z = test.split(' ')
    x = int(x)
    y = int(y)
    z = int(z)
    result = ""
    for i in range(1, z+1):
        if i % x == 0 and i % y == 0:
            result += "FB "
        elif i % x == 0:
            result += "F "
        elif i % y == 0:
            result += "B "
        else:
            result += str(i) + " "
    print result.rstrip()

test_cases.close()
