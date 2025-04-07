from itertools import combinations
from math import prod
from sympy import factorint
from sympy.ntheory.modular import crt

limit = 10**7
ans = 0

def A182665(n):
    if n == 1:
        return 0
    plist = tuple(p**q for p, q in factorint(n).items())
    if len(plist) == 1:
        return 1
    else:
        return n-int(min(min(crt((m, n//m), (0, -1))[0], crt((n//m, m), (0, -1))[0]) for m in (prod(d) for l in range(1, len(plist)//2+1) for d in combinations(plist, l))))

for n in range(1, limit+1):
    ans += A182665(n)
