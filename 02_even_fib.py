def fib(max):
    x = 1
    y = 1

    while y < max:
        if y % 2 == 0:
            yield y

        temp = x
        x = y
        y = x + temp

print list(fib(4000000))
print sum(fib(4000000))
