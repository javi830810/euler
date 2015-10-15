__author__ = 'jdepaula'
import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    sentence = test.strip()

    if len(sentence) <= 55:
        print sentence
    else:
        sentence = sentence[:39]
        print len(sentence)
        sentence = sentence.rstrip()
        print sentence + "... <Read More>"

test_cases.close()
