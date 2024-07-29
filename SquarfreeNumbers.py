limit = 2**25
IsPrime = (limit + 1) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
            
Primes = [k for k in range(2, limit+1) if IsPrime[k]]
limit = limit**2
ans = limit
n = len(Primes)

for i1 in range(n):
    p1 = Primes[i1]
    ans -= limit // p1**2
    
    # We should add the double squares again, subtract triple squares, etc. (11!)**2 > 2**50
    for i2 in range(i1+1, n):
        p2 = Primes[i2]
        p = p1**2 * p2**2
        ans += limit // p
        
        if p > limit:
            break
        
        for i3 in range(i2+1, n):
            p3 = Primes[i3]
            p = p1**2 * p2**2 * p3**2
            ans -= limit // p
            
            if p > limit:
                break
            
            for i4 in range(i3+1, n):
                p4 = Primes[i4]
                p = p1**2 * p2**2 * p3**2 * p4**2
                ans += limit // p
                
                if p > limit:
                    break
                
                for i5 in range(i4+1, n):
                    p5 = Primes[i5]
                    p = p1**2 * p2**2 * p3**2 * p4**2 * p5**2
                    ans -= limit // p
                    
                    if p > limit:
                        break
                    
                    for i6 in range(i5+1, n):
                        p6 = Primes[i6]
                        p = p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2
                        ans += limit // p
                        
                        if p > limit:
                            break
                        
                        for i7 in range(i6+1, n):
                            p7 = Primes[i7]
                            p = p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2 * p7**2
                            ans -= limit // p
                            
                            if p > limit:
                                break
                            
                            for i8 in range(i7+1, n):
                                p8 = Primes[i8]
                                p = p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2 * p7**2 * p8**2
                                ans += limit // p
                                
                                if p > limit:
                                    break
                                
                                for i9 in range(i8+1, n):
                                    p9 = Primes[i9]
                                    p = p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2 * p7**2 * p8**2 * p9**2
                                    ans -= limit // p
                                    
                                    if p > limit:
                                        break
                                    
                                    for i10 in range(i9+1, n):
                                        p10 = Primes[i10]
                                        p = p1**2 * p2**2 * p3**2 * p4**2 * p5**2 * p6**2 * p7**2 * p8**2 * p9**2 * p10**2
                                        ans += limit // p
                                        
                                        if p > limit:
                                            break