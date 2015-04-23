i = 2
j = 2
stop = False
while i < 1000:
    i += 1
    j = 1
    if not stop:
        while j < 1000:
            j += 1
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                print '%s + %s + %s = 1000' % (i, j, k)
                stop = True
                break