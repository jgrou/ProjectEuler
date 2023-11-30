import math

ans = 0

for n in range(23,101):
    for r in range(int(n/2)):
        if  math.comb(n,r) > 10**6:
            ans += n + 1 - 2 * r
            break