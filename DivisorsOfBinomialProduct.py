import math

mod = 1_000_000_007 # This better be prime
limit = 20_000

IsPrime = (limit+1) * [True]
for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

Primes = [p for p in range(2, limit+1) if IsPrime[p]]

def PrimeFactorization(n):
    res = {}
    for p in Primes:
        if p**2 > n:
            break
        if n%p == 0:
            res[p] = 0
            while n%p == 0:
                res[p] += 1
                n //= p
    if n >1:
        res[n] = 1
    return res

Factorization = (limit+1) * [None]
for n in range(2, limit+1):
    Factorization[n] = PrimeFactorization(n)

def B(n):
    res = {}
    for k in range(2,n+1):
        power = 2*k-1-n # A001142 - OEIS
        for prime, exp in Factorization[k].items():
            if prime in res:
                res[prime] += exp*power
            else:
                res[prime] = exp*power
    return res

def modinv(a, m):
    """Modular inverse using Fermat's Little Theorem (m must be prime)"""
    return pow(a, m - 2, m)

def D(n):
    result = 1
    for p, e in B(n).items():
        numerator = pow(p, e + 1, mod) - 1
        denominator = modinv(p - 1, mod)
        term = (numerator * denominator) % mod
        result = (result * term) % mod
    return result

def S(n):
    res = 0
    for k in range(1,n+1):
        res = (res + D(k))%mod
    return res

print(S(limit))
