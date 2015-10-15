__author__ = 'jdepaula'

import sys
import math


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    x, y = test.split(':')
    l = x.split(' ')
    positions = y.split(',')

    for pos in positions:
        i,j = pos.split('-')
        i = int(i)
        j = int(j)
        l[i], l[j] = l[j], l[i]
    print ' '.join(l)

test_cases.close()
