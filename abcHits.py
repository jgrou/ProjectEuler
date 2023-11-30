def IsPrime(n):
    if n < 2:
        return False
    for p in primes:
        if n%p == 0:
            return False
        if p > int(n**0.5):
            break
    return True

def prime_facotrization(r):
    divisors = set()
    for p in primes:
        while r%p == 0:
            r /= p
            divisors.add(p)
        if r == 1:
            break
    return divisors

N = 120_000
primes = []
prime_factors = {}
radical = {}
ans = 0

for c in range(1,N):
    if IsPrime(c):
        prime_factors[c] = {c}
        primes.append(c)
    else:
        prime_factors[c] = prime_facotrization(c)
    
    c_factor = prime_factors[c]
     
    rad = 1
    for factor in c_factor:
        rad *= factor
 
    radical[c] = rad
           
    for b in range(int(c/2)+1, c):
        b_factor = prime_factors[b]
        if len(c_factor.intersection(b_factor)) > 0:
            continue
        
        if radical[c-b] * radical[b] * radical[c] < c:
            ans += c