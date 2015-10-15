sequence = [-1, -8, 3, 2, -4, 5]

def Kadane(sequence):
    max_so_far = max_ending_here = -100000

    for x in sequence:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print Kadane(sequence)
