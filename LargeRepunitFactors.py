def IsPrime(n):
    if n<2:
        return False
    for p in primes:
        if n%p == 0:
            return False
        if p > int(n**0.5):
            break
    return True

primes = []
N = 10
p = 2
factorization = []

while p <= N:
    if IsPrime(p):
        primes.append(p)
        while N%p == 0:
            N = N // p   
            factorization.append(p)
    p += 1
    
while len(primes) < 50:
    if IsPrime(p):
        primes.append(p)
    p += 1