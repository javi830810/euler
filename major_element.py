__author__ = 'jdepaula'

import sys
import math


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    elements = test.split(',')
    found = False
    index = {}
    for x in elements:

        if index.get(x, False):
            continue
        count = 0
        for y in elements:
            if y == x:
                count += 1
        if count > len(elements)/2:
            print x
            found = True
            break
        index[x] = True
    if not found:
        print None

test_cases.close()
