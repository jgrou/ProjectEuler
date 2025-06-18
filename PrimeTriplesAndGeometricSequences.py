import math

n = 10**8
ans = 0
IsPrime = (n+1) * [True]
IsPrime[0] = False
IsPrime[1] = False

for p in range(2, int(n**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, n+1, p):
            IsPrime[k] = False

for x in range(2, math.ceil(n**0.5)):
    for k in range(1, math.ceil(n/x**2)):
        c = k * x**2 - 1
        if IsPrime[c]:
            for y in range(1,x):
                if math.gcd(x,y) == 1:
                    b = k * x * y - 1
                    a = k * y**2 - 1
                    if IsPrime[b] and IsPrime[a]:
                        ans += a+b+c
        


