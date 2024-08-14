from sympy import divisors

limit = 100_000_000

IsPrime = (limit + 2) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

def PrimeGeneratingIntegers(n):
    for d in divisors(n):
        p = n//d + d
        if not IsPrime[p]:
            return False
    return True

ans = 1 # 1 is the only odd number for which this holds

for n in range(2, limit+1, 2):
    if IsPrime[n+1]:
        if PrimeGeneratingIntegers(n):
            ans += n