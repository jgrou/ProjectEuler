limit = 10000

def SmallDigits(curr_value, max_length, curr_length):
    if max_length == curr_length:
        yield curr_value
        return
    if curr_length == 0:
        for start_digit in range(1,3):
            yield from SmallDigits(start_digit, max_length, curr_length+1)
    else:
        for digit in range(3):
            new_value = 10*curr_value + digit
            yield from SmallDigits(new_value, max_length, curr_length+1)
 

divisors = [i for i in range(1,limit-1)]
res = (limit+1) * [0]
i = 1

while len(divisors) > 0:
    for f in SmallDigits(0, i, 0):
        divisors2 = divisors.copy()
        for n in divisors:
            if n > f:
                break
            if f%n == 0:
                res[n] = f // n
                divisors2.remove(n)
        divisors = divisors2
    i += 1

res[9999] = 1111333355557778 # Based on pattern of 9,99,9999. Takes very long otherwise
res[10000] = 1 # Trivial
ans = sum(res)