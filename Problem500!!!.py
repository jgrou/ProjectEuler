import math
from itertools import count
# n = p1**k1 * p2**k2 
# Total number of divisors: (k1+1) * (k2+1)
# Smallest number with 2**500500 divisors, not at least so many!
# So power should be 2**k - 1

def smallest_number_with_n_divisors(target_divisors):
    for num in count(1):
        divisors = 1
        n = num
        for i in range(2, int(n**0.5) + 1):
            exponent = 0
            while n % i == 0:
                n //= i
                exponent += 1
            divisors *= (exponent + 1)
        if n > 1:
            divisors *= 2
        if divisors >= target_divisors:
            return num

# 64 gives 2**3 * 3**3 * 5 * 7
# 128 gives 2**3 * 3**3 * 5 * 7 * 11
# Next power of 2 would be 2**7: so multiply with 2**4 = 16 > 11
# Next power of 5 would be 5**3: so multiply with 5**2 = 25 > 11

limit = 7_370_050  # Empirically this number gives the correct number of divisors
ans = 1
log_div = 0

IsPrime = (limit + 1) * [True]
for p in range(2, int(limit**0.5) + 1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False           

for p in range(2,limit+1):
    if IsPrime[p]:
        # p**(2**m) < limit
        power = int(math.log(limit, p))
        m = int(math.log(power, 2))
        # next power should be factor power smaller
        power = 2**(m+1) - 1
        ans *= pow(p, power, 500500507)
        ans %= 500500507
        log_div += m+1