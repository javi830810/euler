

def to_binary(n):
    if n <= 1:
        return [n]
    return to_binary(n>>1) + [n%2]

print to_binary(3)
print to_binary(4)
print to_binary(5)
print to_binary(6)
print to_binary(10)
print to_binary(128)
print to_binary(256)
