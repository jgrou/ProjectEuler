import math

N = 1000000
primes = []
CircularPrimes = []
x = 2

while x<N:
    prime = True
    for p in primes:
        if p > math.sqrt(x):
            break
        elif x%p==0:
            prime = False
            break
    if prime == True:
        primes.append(x)
    x+=1
    
for p in primes:
    circular = True
    rotation = p
    for _ in range(len(str(p))):
        rotation = str(rotation)[1:] + str(rotation)[0]
        if int(rotation) not in primes:
            circular = False
            break
    if circular:
        CircularPrimes.append(p)
    
ans = len(CircularPrimes)
        