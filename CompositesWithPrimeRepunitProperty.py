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
n = 1
ans = 0
i = 0

while i < 25:
    n += 1
    if n%2 == 0 or n%5==0:
        continue
    
    if IsPrime(n):
        primes.append(n)
    else:
        An = 1
        R = 1
        while R%n > 0:
            R = (10 * R + 1) % n
            An += 1
        if (n-1)%An == 0:
            ans += n
            i += 1