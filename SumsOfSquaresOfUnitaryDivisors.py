import math

# If n = p1**pow1 * p2**pow2 * ... * pk**powk
# We should seperate all the p: we can pick every number or not

limit = 100_000_000
mod = 1_000_000_009 # This must be prime
ans = 1

IsPrime = (limit + 1) * [True]
for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

# Use Legendre's formula to find prime factorization of n!
for p in range(2, limit+1):
    if IsPrime[p]:
        k = 1
        e = 0
        while p**k < limit:
            e += limit // p**k
            k += 1

        ans *= (1 + pow(p, 2*e, mod))
        ans %= mod
