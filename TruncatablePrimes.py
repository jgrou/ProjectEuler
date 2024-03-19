TruncatablePrimes = []
primes = [2,3,5,7]
x = 11

while len(TruncatablePrimes) < 11:
    prime = True
    for p in primes:
        if p > x**0.5:
            break
        elif x%p==0:
            prime = False
            break
    if prime == True:
        primes.append(x)
        
        # Now check if truncatable as well
        left = x
        right = x
        
        if x > 9:
            for i in range(len(str(x))-1):
                left = int(str(left)[1:])
                if left not in primes:
                    prime = False
                    break
                right = int(str(right)[:-1])
                if right not in primes:
                    prime = False
                    break
            
        if prime == True:
            TruncatablePrimes.append(x)
    
    x+=1
  
ans = sum(TruncatablePrimes)
