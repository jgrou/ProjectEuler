from math import prod
from sympy import factorint

def a(n): # https://oeis.org/A046079
    res = 1
    for p, e in factorint(n).items():
        if p == 2:
            res *= (2*e - 1)
        else:
            res *= (2*e + 1)
    return res >> 1 # Bitwise right shift: integer division by 2

# res should be 2*limit of 2 * limit+1
# res is always odd

limit = 47547
s = 2 * limit + 1
f = factorint(s)
Primes = [2,3,5,7,11] # sum(f,values())=5, so we need the first 5 primes
keys = list(f)
keys.sort(reverse=True)  # Smallest prime should have biggest power
i = 0
ans = 1

for p in keys:
    for _ in range(f[p]):
        if i == 0:
            power = p//2 + 1
        else:
            power = p//2
        ans *= Primes[i]**power
        i += 1
