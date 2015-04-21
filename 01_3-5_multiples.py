def multiples(max):
    for x in range(1,max):
        if x % 3 == 0 or x % 5 == 0:
            yield x

print sum(multiples(1000))
