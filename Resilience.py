def IsPrime(k):
    for p in primes:
        if k%p == 0:
            return False
        if p > k**0.5:
            break
    return True
    
primes = []

for n in range(2,100): # Guess that 100 is enough
    if IsPrime(n):
        primes.append(n)

n = 4
PrimeProduct = primes[0]
NewPrimeProduct = primes[0] * primes[1]
i = 2
step = 2
NumberOfResilientFractions = 2

# Let p be the next prime factor
# #(resilient factors k * primeproduct) = k * #(resilient factors of prime product), for k < p
# #(resilient factors p * primeproduct) = (p-1) * #(resilient factors of prime product)

while True:
    if 94744 * NumberOfResilientFractions < 15499 * (n-1):
        break
    
    n += PrimeProduct
    
    if n == NewPrimeProduct:
        PrimeProduct = NewPrimeProduct
        NewPrimeProduct *= primes[i]
        i += 1
        step = NumberOfResilientFractions
    else:
        NumberOfResilientFractions += step