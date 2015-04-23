def factors(n):
    return filter(lambda i: n % i == 0, range(1, n))

def increase(x, y):
    y_factors = factors(y)
    print x
    print y_factors
    for i in y_factors:
        if x % i != 0:
            x = x*i
    return x


def smallest_multiple(max):
    number = 1
    for x in range(1,max+1):
        number = increase(number, x)
    return number


print factors(20)

#print smallest_multiple(10)

#print smallest_multiple(10)
