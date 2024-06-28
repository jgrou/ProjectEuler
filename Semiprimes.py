limit = 10**8

# Calculate all primes up to limit/2
n = limit // 2
is_prime = [True] * (n + 1)

for p in range(2, int(n**0.5) + 1):
    if is_prime[p]:
        for i in range(p * p, n + 1, p):
            is_prime[i] = False

primes = [p for p in range(2, n + 1) if is_prime[p]]
            
# Calculate number of prime factors
ans = 0
prime_divisors = [0] * (limit + 1) # Every number is divisible by 1 and itself

for p in primes:
    for i in range(p, limit+1, p):
        prime_divisors[i] += 1
    # Count once more for the squares
    for i in range(p**2, limit+1, p**2):
        prime_divisors[i] += 1
    # Count once more for the cubes
    for i in range(p**3, limit+1, p**3):
        prime_divisors[i] += 1
    # Higher orders we do not care, since we only need to know if the number of prime factors is more than 2
        
semiprimes = [i for i in range(2,limit+1) if prime_divisors[i]==2]