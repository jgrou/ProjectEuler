limit = 40_000_000

# Sieve of Erasthotenes
is_prime = [True] * (limit + 1)

for p in range(2, int(limit**0.5) + 1):
    if is_prime[p]:
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False

primes = [p for p in range(2, limit + 1) if is_prime[p]]

def phi(n) :
    '''Euler's Totient Function using Euler's product formula'''
    if is_prime[n]: # For primes, all numbers k <=n have gcd(k,n) = 1 so phi(n) = n -1
        return n-1
    
    result = n   # Initialize result as n
     
    # Consider all prime factors of n and for every prime factor p, multiply result with (1 - 1 / p)
    for p in primes:
        if p**2 > n:
            break
        # Check if p is a prime factor.
        if n % p == 0 :
            # If yes, then update n and result
            while n % p == 0 :
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
        
    # If n has a prime factor greater than sqrt(n) (There can be at-most one such prime factor)
    if n > 1 :
        result -= result // n
    # Since in the set {1,2,....,n-1}, all numbers are relatively prime with n if n is a prime number
 
    return int(result)
    
# Compute answer
ans = 0
for p in primes:
    n = p
    count = 1
    while n > 1:
        n = phi(n)
        count += 1
    if count == 25:
        ans += p