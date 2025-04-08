# There should be 100_000 primes between 10**14 and 10**14 + 10**7
start = 10**14
end = 10**7
PrimeLimit = int((start+end)**0.5)+1

IsPrime = (PrimeLimit+1) * [True]
for p in range(2, int(PrimeLimit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, PrimeLimit+1, p):
            IsPrime[k] = False

Primes = [p for p in range(2, PrimeLimit+1) if IsPrime[p]]

# Now use these primes to find the primes between 10**14 and 10**14 + 10**7
IsPrime = (end + 1) * [True]
for p in Primes:
    # First number bigger than start that divides p
    i = (start // p + 1) * p
    while i < start + end:
        IsPrime[i - start] = False
        i += p

a = [p for p in range(start+1, start+end) if IsPrime[p-start]]
a = [None] + a[:100_000]

MOD = 1234567891011
ans = 0

def fib_mod(n):
    def helper(n):
        if n == 0:
            return (0, 1)
        a, b = helper(n // 2)
        c = (a * ((2 * b - a) % MOD)) % MOD
        d = (a * a + b * b) % MOD
        return (c, d) if n % 2 == 0 else (d, (c + d) % MOD)
    
    return helper(n)[0]

for n in range(1, 100_001):
    ans += fib_mod(a[n])

ans %= MOD
