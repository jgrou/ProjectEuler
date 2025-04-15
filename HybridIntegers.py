# Max_p: 2**p * p**2 <= 800800**800800
import math

limit = 800800 * math.log(800800,2)
PrimeLimit = int(limit)
IsPrime = (PrimeLimit+1)*[True]

for p in range(2, int(PrimeLimit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, PrimeLimit+1, p):
            IsPrime[k] = False

Primes = [p for p in range(2, PrimeLimit+1) if IsPrime[p]]
i = len(Primes) - 1
q = Primes[i]
ans = 0

for j, p in enumerate(Primes):
    while p * math.log(q,2) + q * math.log(p,2) > limit:
        i -= 1
        q = Primes[i]
    if i > j:
        ans += i-j
    else:
        break
