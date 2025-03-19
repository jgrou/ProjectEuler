import math
k = 90  # First k s.t. 2**k starts with 123
i = 1

def Check(k):
    n_digit = k * math.log(2, 10)
    return int(10**(n_digit - int(n_digit) + 2)) == 123

while i < 678910:
    for diff in [196,289,485]:  # These are the only differences that occur
        if Check(k+diff):
            k += diff
            i += 1
            break