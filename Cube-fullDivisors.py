import math
from sympy import factorint, integer_nthroot

limit = 10**18
ans = 0

for x in range(1, integer_nthroot(limit,5)[0] +1):
    if all(d<=1 for d in factorint(x).values()):
        rest = limit // x**5
        for y in range(1, integer_nthroot(rest,4)[0] + 1):
            if math.gcd(x,y) == 1 and all(d<=1 for d in factorint(y).values()):
                rest2 = rest // y**4
                for z in range(1, integer_nthroot(rest2,3)[0] + 1):
                    n = x**5 * y**4 * z**3
                    ans += limit // n

print(ans)