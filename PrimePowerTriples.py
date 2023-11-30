def IsPrime(n):
    for p in primes:
        if n % p == 0:
            return False
        if p > n**0.5:
            break
    return True

primes = []
k = 2
PrimePowerTriples = []
k_max = int(50_000_000**0.5)

for k in range(2, k_max+1):
    if IsPrime(k):
        primes.append(k)
        for p1 in primes:
            for p2 in primes:
                PrimePowerTriple = k**2 + p1**3 + p2**4
                if PrimePowerTriple < 50_000_000:
                    PrimePowerTriples.append(PrimePowerTriple)
                else:
                    break
        if k < 50_000_000**(1/3):  
            for p1 in primes:
                for p2 in primes:
                    PrimePowerTriple = p1**2 + k**3 + p2**4
                    if PrimePowerTriple < 50_000_000:
                        PrimePowerTriples.append(PrimePowerTriple)
                    else:
                        break
        if k < 50_000_000**(1/4):  
            for p1 in primes:
                for p2 in primes:
                    PrimePowerTriple = p1**2 + p2**3 + k**4
                    if PrimePowerTriple < 50_000_000:
                        PrimePowerTriples.append(PrimePowerTriple)
                    else:
                        break
                    
ans = len(set(PrimePowerTriples))