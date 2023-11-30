n = 2
primes = []
distinct = [0,0]

while True:
    prime = True
    factorization = []
    x = n
    
    for p in primes:
        while x%p == 0:
            x = x/p
            factorization.append(p)
            prime = False
        if x == 1:
            break
        
    if prime:
        primes.append(x)
        
    distinct.append(len(set(factorization)))
    if distinct[n] == 4:
        if distinct[n-1] == 4:
            if distinct[n-2] == 4:
                if distinct[n-3] == 4:
                    ans = n-3
                    break
        
    n += 1