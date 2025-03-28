import math
# https://oeis.org/A064602
limit = 10**15

def f(n):
    return n*(n+1)*(2*n+1)//6

def a(n):
    s = math.isqrt(n)
    return sum(f(n//k) + k*k*(n//k) for k in range(1, s+1)) - s*f(s)

print(a(limit)%10**9)
