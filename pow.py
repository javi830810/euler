
def pow(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 1:
        return pow(a,b/2)*pow(a,b/2)*a
    if b % 2 == 0:
        return pow(a,b/2)*pow(a,b/2)


print pow(2,5)
