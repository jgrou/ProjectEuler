import math
from sympy import n_order

n_zeros = 8

# Starting with 8 zeros means p > 10**8
# Starting with a 137 means p > 10**9 / 1.37 and p < 10**9 / 1.38
# Number is of form (10**(p-1) - 1) / p
# So ending with 56789, means p*56789 should be ending with 99999

start_p = math.ceil(10**9/1.38)
end_p = int(10**9/1.37)

limit = int(end_p**0.5)
IsPrime = (limit+1) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

primes = [p for p in range(2, limit+1) if IsPrime[p]]

IsPrime = (end_p - start_p + 1) * [True]

for p in primes:
    start = (start_p // p) * p
    if start < start_p:
        start += p
    for k in range(start, end_p+1, p):
        IsPrime[k-start_p] = False

new_primes = [p for p in range(start_p,end_p+1) if IsPrime[p-start_p]]
              
for P in new_primes:
    if (P*56789)%10**5 == 99999:
        if n_order(10, P) == P-1:
            r = 10**n_zeros
            ans = 0

            while r != 1:
                x = 10*r
                d = int(x/P)
                r = x%P
                ans += d
