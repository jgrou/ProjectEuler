start = 1_000_000_000
end = 100_000_000

PrimeLimit = int((start+end)**0.5)+1

IsPrime = (PrimeLimit+1) * [True]
for p in range(2, int(PrimeLimit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, PrimeLimit+1, p):
            IsPrime[k] = False

Primes = [p for p in range(2, PrimeLimit+1) if IsPrime[p]]

# Now use these primes to find the primes between start and start + end
IsPrime = (end + 1) * [True]
for p in Primes:
    # First number bigger than start that divides p
    i = (start // p + 1) * p
    while i < start + end:
        IsPrime[i - start] = False
        i += p

LargePrimes = [p for p in range(start+1, start+end) if IsPrime[p-start]]

product = 1
for x in range(LargePrimes[0]):
    product *= (x**3 - 3*x + 4)%LargePrimes[0]
    product %= LargePrimes[0]
