import math

is_prime_x = lambda x : len(filter(lambda y: x%y == 0, range(1, int(math.sqrt(x)) + 1))) == 1

def n_prime(n):
    count = 0
    index = 2
    while True:
        if is_prime_x(index):
            count += 1
        if count == n:
            break
        index += 1
    return index


print n_prime(10001)
