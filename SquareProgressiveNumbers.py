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
            
# untill i = 116_946 gives 34181672531

ans = 0

for d in range(1, int(limit**0.5)+1):
    found = False
    for y in range(int(d**0.5), 1, -1):
        if found:
            break
        for factor in range(1, int(d/y**2)+1):
            r = factor * y**2
            n = d**3 / r + r
            
            if n > 2 * limit:
                break
            if n > limit:
                continue
            if not int(n**0.5)**2 == n:
                continue
            q = n / d
            if d * q + r != n:
                continue
            
            ans += n
            found = True
            break
        y -= 1