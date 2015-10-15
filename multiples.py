__author__ = 'jdepaula'

import sys
import math


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    x, y = test.split(',')
    x = int(x)
    y = int(y)

    for i in range(2, 10**6):
        if y*i >= x:
            print y*i
            break

test_cases.close()
