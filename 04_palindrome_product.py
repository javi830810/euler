def is_palindrome(x):
    x = str(x)
    for i in range(0,len(x)):
        if x[i] != x[len(x)-1-i]:
            return False
    return True

def max_palindrome_in_range(min,max):
    result = 0
    for x in range(min,max):
        for y in range(min,max):
                if is_palindrome(x*y) and x*y > result:
                    result = x*y
    return result

print max_palindrome_in_range(100,999)
