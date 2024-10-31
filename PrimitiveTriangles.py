import math
limit = 2_000
ans = 0
'''
IsPrime = (limit+1) * [True]
Factors = {}

for i in range(2, limit+1):
    Factors[i] = set()

for p in range(2, limit+1):
    if IsPrime[p]:
        for k in range(p, min(p**2,limit)+1, p):
            Factors[k].add(p)
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
            Factors[k].add(p)
'''
for c in range(1, (limit+1)//2):
    max_b = min(c, limit - c - 1) # a+b+c <= limit and a >= 1
    min_b = max(1, (c+1)//2) # b >= a and a + b > c
    
    for b in range(min_b, max_b + 1):
        max_a = min(b, limit - c - b) # a<=b and a+b+c <= limit
        min_a = c-b+1 # a+b > c
        gcd_bc = math.gcd(b,c)
        if gcd_bc == 1:
            ans += max_a + 1 - min_a
            continue
        for a in range(min_a, max_a + 1):
            if math.gcd(a,gcd_bc)==1:
                ans += 1