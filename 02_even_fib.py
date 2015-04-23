def even_fib(max):
    x = 1
    y = 1

    while y < max:
        if y % 2 == 0:
            yield y
        x, y = y, x + y


print sum(even_fib(4000000))
