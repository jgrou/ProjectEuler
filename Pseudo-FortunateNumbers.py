import math

N = 10**9

# Find all primes up to root N
limit = int(N**0.5)
IsPrime = (limit+1) * [True]

for p in range(2, limit):
    if IsPrime[p]:
        for i in range(p * p, limit + 1, p):
            IsPrime[i] = False
           
primes = [p for p in range(2, limit + 1) if IsPrime[p]]

def CheckPrime(n):
    for p in primes:
        if p*p > n:
            return True
        if n%p == 0:
            return False
    return True

# Find all admissable numbers
AdmissableNumbers = set([2**i for i in range(1, int(math.log(N,2))+1)]) # First powers of two
UsedLast = [2**i for i in range(1, int(math.log(N,2))+1)] # Array to check if we use consecutive primes
prime_product = 2 # Product of the first primes

for p in primes[1:]:
    if prime_product*p > N: # Then we cannot add anymore
        break
    
    UsedNew = []
    power = 1
    while True:
        base = p**power
        
        if prime_product*base > N:
            break
        
        for n in UsedLast:
            new_number = n * base
            if new_number > N:
                break
            AdmissableNumbers.add(new_number)
            UsedNew.append(new_number)
        power += 1
        
    UsedLast= UsedNew
    UsedLast.sort()
    prime_product *= p # Do it here to avoid stopping for too low base
    
AdmissableNumbers = list(AdmissableNumbers)
AdmissableNumbers.sort()

# Check PseudoFortunate
pseudoFortunateNumbers = set()
max_prime = max(primes)
ans = 0

for n in AdmissableNumbers:
    m = n+3 
    if m <= max_prime:
        while not IsPrime[m]:
            m += 2 # primes are odd
    else:
        while not CheckPrime(m):
            m += 2
            
    pseudoFortunateNumbers.add(m-n)
    
ans = sum(pseudoFortunateNumbers)