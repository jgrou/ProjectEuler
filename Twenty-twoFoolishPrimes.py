import random
import math

limit = 100
IsPrime = (limit+1)*[True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

Primes = [p for p in range(2,limit+1) if IsPrime[p]]
n_primes = len(Primes)

# Monte Carlo to get intution for the result: more or less 0.0016
ans = 0
disks = list(range(1,limit+1))

for _ in range(10000):
    random.shuffle(disks)
    away = 0
    for p in Primes:
        if disks[p-1] != p:
            away += 1

    if away == 22:
        ans += 1

print(ans/10000)

# Suppose I pick 3 that are correct: comb(25,3) ways
# Then left with 97 position of which we want to avoid 22 fixed points: inclusion–exclusion
ans = 0
for j in range(23):
    ans += (-1)**j * math.comb(22,j) * math.factorial(97-j)

ans *= math.comb(n_primes,3) / math.factorial(100)
print(round(ans,12))

