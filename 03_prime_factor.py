import math

is_prime_x = lambda x : len(filter(lambda y: x%y == 0, range(1, int(math.sqrt(x)) + 1))) == 1

def max_prime_factor(x):
    max = 0
    for y in range(1, int(math.sqrt(x)) + 1):
        if is_prime_x(y) and x%y==0:
            max = y
    return max


print max_prime_factor(600851475143)
