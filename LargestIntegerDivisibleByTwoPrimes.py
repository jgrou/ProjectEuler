import math

limit = 10_000_000
IsPrime = (limit + 1) * [True]
for p in range(2, int(limit**0.5) + 1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False           
Primes = [p for p in range(2,limit+1) if IsPrime[p]]

def M(p, q, N):
    res = 0
    if p * q > N:
        return 0
    for n in range(1, int(math.log(N, p))):
        m = int(math.log(N / p**n, q))
        if m > 0:
            res = max(res, p**n * q**m)
            
    return res

S = set()

for i,p in enumerate(Primes):
    if p**2 > limit:
        break
    for q in Primes[i+1:]: # q > p
        if p*q > limit:
            break
        S.add(M(p,q,limit))
        
ans = sum(S)