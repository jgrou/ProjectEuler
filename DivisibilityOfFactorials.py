import math

limit = 10**8
s = (limit+1) * [0]
IsPrime = (limit + 1) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

for n in range(2, limit+1):
    if IsPrime[n]:
        max_power = int(math.log(limit, n))
        if max_power <= n:
            for power in range(1, max_power+1):
                k = n**power
                s[k] = power * n
                # If n = p1^e1 * p2^e2 * ... * pk^ek, then s(n) = max( s(p1^e1), s(p2^e2), ..., s(pk^ek) )
                k += n**power
                while k <= limit:
                    s[k] = max(power*n, s[k])
                    k += n**power
        else:
            max_m = int(math.log(max_power,n)) + 1
            for power in range(1, max_power+1):
                m = 0
                res = 0
                while res < power:
                    m += n
                    res = 0
                    for k in range(1, max_m + 1):
                        res += m // n**k

                k = n**power   
                s[k] = m
                k += n**power
                while k <= limit:
                    s[k] = max(m, s[k])
                    k += n**power
                    
print(sum(s))
