s = 'abcde'

#IN Place
#s = list(s)
# for x in xrange(0,len(s)):
#     y = len(s) - 1 - x
#     if y <= x:
#         break
#     s[x],s[y] = s[y],s[x]
# print "Reverse: %s" % reduce(lambda x,y: x+y, s)

#Iterative
# reverse = ""
# for x in range(len(s)-1, -1, -1):
#     reverse += s[x]
#
# print reverse


def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

print reverse(s)
