def count_factors(n):
    return len([i for i in range(1, n//2 + 1) if not n%i] + [n])

def triangular(index):
    return index*(index+1)/2

index = 1
while True:

    factors_x = count_factors(index)
    factors_x_1 = count_factors(index+1)

    triangular_factors = factors_x * (factors_x_1 - 1) + 1

    if triangular_factors >= 500:
        #Make the final definitive check
        if count_factors(triangular(index)) >= 500:
            print triangular(index)
            break

    index += 1
