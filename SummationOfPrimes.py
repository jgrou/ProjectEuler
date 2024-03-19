N = 2000000
primes = []
x = 2

while x<N:
    prime = True
    for p in primes:
        if p > x**0.5:
            break
        elif x%p==0:
            prime = False
            break
    if prime == True:
        primes.append(x)
    x+=1
    
ans = sum(primes)
