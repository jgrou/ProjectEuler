limit = 10**12
ans = 9 # We skip x=1 in the loop, so we have to add this answer

# r has to be a perfect power

for i in range(2, int(limit**0.5)):
    n = i**2
    min_d = int((n-1)**(1/3)) # max_d = i
    found = False
    # d is the mutiple of a square: d=m*k^2
    for k in range(2, int(i**0.5)+1):
        m = max(int(min_d / k**2),1)
        d = m * k**2
        
        while d < i:
            q = n // d
            r = n % d
            if q*r == d**2: # r < d < q
                print(n,i,q,d,r)
                ans += n
                found = True
                break # Once we find that n is progressive we do not need to check other d's
                
            m += 1
            d = m * k**2
        
        if found:
            break