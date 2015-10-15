def print_fib(n):
    n_2 = 1
    n_1 = 1
    for x in xrange(0,n):
        if x == 0:
            print 1
        elif x == 1:
            print 1
        else:
            n_2, n_1 = n_1, n_1 + n_2
            print n_1

print_fib(8)
