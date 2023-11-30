import math
primes = []
x = 1
ans = 0
conjecture = True

while conjecture:
    x += 1
    
    prime = True
    
    for p in primes:
        if p > math.sqrt(x):
            break
        if x%p == 0:
            prime = False
            break
        
    if prime:
        primes.append(x)
        
    elif x%2 == 1:
        # Now we are composite and odd
        conjecture = False
        
        for p in primes:
            if math.sqrt((x-p)/2) % 1 == 0:
                conjecture = True
                break