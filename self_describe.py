__author__ = 'jdepaula'
import sys
import math

test_cases = open(sys.argv[1], 'r')


def _count(number, digit):
    count = 0
    for x in number:
        if digit == x:
            count += 1
    return count

for test in test_cases:
    number = test.strip()

    found = True
    for index in range(0, len(number)):
        if not _count(number, str(index)) == int(number[index]):
            found = False
            break
    print int(found)

test_cases.close()
