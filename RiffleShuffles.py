def riffle(pos, n):
    if pos <= n//2:
        return 2 * pos - 1
    else:
        return 2 * pos - n

def s(n):
    res = 0
    seen = set()
    
    for i in range(1, n+1):
        if i in seen:
            continue
        length = 0
        x = i
        while x not in seen:
            seen.add(x)
            x = riffle(x, n)
            length += 1
        res = max(res, length)
        
    return res

# https://oeis.org/A002326: The numbers 2n+2 s.t. 60 is the least m s.t. 2n+1 divides 2**m - 1
from sympy import divisors

limit = 60
div_set = set()
ans = 0

for m in range(1, limit):
    for d in divisors(2**m - 1):
        div_set.add(d)

for d in divisors(2**limit - 1):
    if d in div_set:
        continue
    if d&1:
        ans += d+1
