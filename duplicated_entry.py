__author__ = 'jdepaula'
import sys

from itertools import permutations
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    p = [ ''.join(p) for p in permutations(test)]
    p.sort()
    result = ''
    for x in p:
        result += '%s,' % x
    print result.rstrip(',')

test_cases.close()
