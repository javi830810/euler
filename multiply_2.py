__author__ = 'jdepaula'
import sys
import math

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.rstrip()

    l1s, l2s = test.split('|')

    l1 = l1s.rstrip().split(' ')
    l2 = l2s.lstrip().split(' ')

    result = ''

    for x in range(0,len(l1)):
        result += str(int(l1[x])*int(l2[x])) + ' '

    print result.rstrip()

test_cases.close()
