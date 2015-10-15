__author__ = 'jdepaula'
import sys
import math

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.rstrip()

    p1, p2 = test.split(') (')

    p1 = p1.lstrip('(')
    p2 = p2.rstrip(')')

    p1x,p1y = p1.split(',')
    p2x,p2y = p2.split(',')
    p1x = int(p1x)
    p2x = int(p2x)
    p1y = int(p1y)
    p2y = int(p2y)
    print int(math.sqrt((p2x - p1x)**2 + (p2y - p1y)**2))

test_cases.close()
