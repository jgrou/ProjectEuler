import math

N = 10001
n = 0
primes = []
x = 2

while n<N:
    prime = True
    for p in primes:
        if p > math.sqrt(x):
            break
        elif x%p==0:
            prime = False
            break
    if prime == True:
        primes.append(x)
        n+=1
    x+=1
    