s = 'abcde'

unique = True
for x in xrange(0,len(s)):
    for y in xrange(0,len(s)):
        if s[x] == s[y] and x != y:
            unique = False
            break
    if not unique:
        break

print "Unique: %s" % unique
