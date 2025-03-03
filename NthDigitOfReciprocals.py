from math import gcd
from functools import reduce

n = 10**7
s = 0

# First do primes necessary for euler totient to speed up
limit = int(n**0.5)
IsPrime = (limit + 1) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
            
primes = [p for p in range(2,limit+1) if IsPrime[p]]

def prime_factorization(n):
    """Returns the prime factorization of 'n' using a list of primes."""
    factors = {}
    for p in primes:
        if p * p > n:
            break
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count > 0:
            factors[p] = count
    if n > 1:  # n is prime
        factors[n] = 1
    return factors

def carmichael(n):
    factors = prime_factorization(n)  # Get prime factorization as {p: k}
    
    def lambda_prime_power(p, k):
        return (p - 1) * p**(k - 1)
    
    # Compute λ(n) as lcm of λ(p^k) for each prime power
    lambdas = [lambda_prime_power(p, k) for p, k in factors.items()]
    
    return reduce(lambda x, y: (x * y) // gcd(x, y), lambdas)

for k in range(2, n+1): # k=1 always gives 0
    x = k
    count2, count5 = 0, 0
    while x&1 == 0:
        x //= 2
        count2 += 1
    while x%5==0:
        x//= 5
        count5 += 1
    if x > 1:
        m = max(count2, count5) # After this many digits, there starts a repetition
        phi = carmichael(x) # This is the length of the repition
        power = (n-m) % phi
        if power == 0:
            power += phi
        power += m
        d = int((10**power // k) % 10)
        s += d
    
print(s)