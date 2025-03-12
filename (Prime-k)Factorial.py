limit = 10**8
ans = 0

IsPrime = (limit + 1) * [True]
for p in range(2, int(limit**0.5) + 1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False           
Primes = [p for p in range(2,limit+1) if IsPrime[p]]

for p in Primes[2:]:
    S = 0
    # (p-1)! = -1 mod p = p-1 mod p
    # (p-2)! = 1 mod p
    # So adding (p-1)! and (p-2)! gives 0 mod p
    # a**(-1) = a**(p-2) mod p
    for k in range(3,6):
        f = 1
        for i in range(2, k):
            f *= pow(p-i,p-2,p)
        S += f
    S %= p
    ans += S