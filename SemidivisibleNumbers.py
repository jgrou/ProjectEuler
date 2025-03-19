limit = 999966663333
ans = 0

PrimeLimit = int(limit**0.5)+1
IsPrime = (PrimeLimit+1)*[True]
for p in range(2, int(PrimeLimit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, PrimeLimit+1, p):
            IsPrime[k] = False
            
Primes = [p for p in range(2,PrimeLimit+1) if IsPrime[p]]

# We need one extra prime
def Prime(n):
    for p in Primes:
        if p**2 > n:
            return True
        if n%p == 0:
            return False
        
while not Prime(PrimeLimit):
    PrimeLimit += 1

Primes.append(PrimeLimit)

for i,p in enumerate(Primes[:-1]):
    p2 = Primes[i+1]
    product = p*p2
    # lps(n) = p
    # ups(n) = p2
    # If n=p**2 it is for sure not semidivisible
    for n in range(p**2 + p, p2**2, p):  # Divisible by p  
        if n > limit:
            break
        if n != product:
            ans += n
    for n in range(p2**2 - p2, p**2, -p2):  # Divisible by p2
        if n > limit:
            continue
        if n != product:
            ans += n