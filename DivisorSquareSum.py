from math import prod

limit = 64_000_000
ans = 0
# https://oeis.org/A046655

IsPrime = (limit+1) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
            
Primes = [k for k in range(2,limit+1) if IsPrime[k]]

def Factorint(n):
    res = {}
    for p in Primes:
        if p**2 > n:
            break
        if n%p == 0:
            res[p] = 0
            while n%p == 0:
                res[p] +=1
                n //= p
                
    if n > 1:
        res[n] = 1
    return res

def a(n): 
    return prod((p**(2*e+2)-1)//(p**2-1) for p, e in Factorint(n).items())

for n in range(1, limit):
    sigma = a(n)
    if round(sigma**0.5)**2 == sigma:
        ans += n