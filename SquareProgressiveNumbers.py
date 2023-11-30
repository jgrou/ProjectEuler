limit = 10**12
ans = 0

for i in range(2, int(limit**0.5)):
    n = i**2
    for d in range(int((n-1)**(1/3)), i): 
        q = n // d
        r = n % d
        if q*r == d**2: # r < d < q
            print(n,i,q,d,r)
            ans += n
            break # Once we find that n is progressive we do not need to check other d's
            
# untill i = 116946 gives 34181672531