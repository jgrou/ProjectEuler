import math

limit = 32
E = (limit + 1) * [0]

for n in range(1,limit+1):
    # Use dynamic programming to find next one
    res = 2**n
    for i in range(n):
        res += math.comb(n,i) * E[i]
    E[n] = res / (2**n - 1)
    
print(round(E[limit],10))