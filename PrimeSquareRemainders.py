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
k = 0
prod = 0
n = 0

while prod < 10**10:
    k += 1
    if IsPrime(k):
        primes.append(k) 
        n += 1
        if n%2 == 1:
            prod = 2 * k * n
        else:
            prod = 2