import math

limit = 51
IsPrime = (limit + 1) * [True]
for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k]= False
Primes = [p for p in range(2,limit+1) if IsPrime[p]]
squarefree = {1}

def SquareFree(k):
    for p in Primes:
        if k%p**2 == 0:
            return False
    return True

for n in range(2, limit): # First two rows are only 1
    max_k = n//2
    for k in range(1, max_k+1): # First column is always 1
        comb = math.comb(n, k)
        if SquareFree(comb):
            squarefree.add(comb)

ans = sum(squarefree)