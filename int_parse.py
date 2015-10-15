def is_int(c):
    return ord(c) >= 48 and ord(c) <= 58

def get_int(c):
    return ord(c) - 48

def int_to_parse(input):
    result = 0
    for x in xrange(0, len(input)):
        character = input[x]
        if not is_int(character):
            raise Error("Invalid Input")

        result += get_int(character) * (10**(len(input) - x - 1))
    return result

print int_to_parse("123456")
