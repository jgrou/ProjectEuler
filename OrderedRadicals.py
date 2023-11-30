import pandas as pd

def IsPrime(n):
    if n < 2:
        return False
    for p in primes:
        if n%p == 0:
            return False
        if p > int(n**0.5):
            break
    return True

primes = []

def prime_facotrization(r):
    divisors = set()
    for p in primes:
        while r%p == 0:
            r /= p
            divisors.add(p)
        if r == 1:
            break
    return divisors

N = 100_000
radical = pd.DataFrame({'n': range(1,N+1), 'rad': N * [0]})

for n in range(1,N+1):
    if IsPrime(n):
        radical['rad'][n-1] = n
        primes.append(n)
    else:
        d = prime_facotrization(n)
        rad = 1
        for i in d:
            rad *= i
        radical['rad'][n-1] = rad
        
smaller = len(radical[radical['rad'] < 1947])
equal = radical[radical['rad'] == 1947]
ans = equal['n'].iloc[9999 - smaller]
