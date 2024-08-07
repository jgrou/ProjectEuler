n = 20_000_000
k = 15_000_000
ans = 0

# First sieve to find primes
IsPrime = (n+1) * [True]

for p in range(2, int(n**0.5)+1):
    if IsPrime[p]:
        for i in range(p*p,n+1,p):
            IsPrime[i] = False
            
Primes = [i for i in range(2,n+1) if IsPrime[i]]

# Add prime factors for number k to n
for m in range(k+1, n+1):
    # Prime factorization
    for p in Primes:
        while m%p == 0:
            m //= p           
            ans += p
        if p**2 > m:
            break
    if m > 2:
        ans += m

# Subtract prime factors for number 1 to n-k
for m in range(2, n-k+1):
    # Prime factorization
    for p in Primes:
        while m%p == 0:
            m //= p           
            ans -= p
        if p**2 > m:
            break    
    if m > 2:
        ans -= m