import math

def FindPartition(s=0, part=(), l=0, max_d=3):
    if s == 18:
        partitions.add(part)
    if l == 10:
        return
    max_d = min(max_d, 18 - s)
    for d in range(1, max_d+1):
        new_part = part + (d,)
        FindPartition(s+d, new_part, l+1, d)
        
def Orderings(part):
    s = sum(part)
    res = 1
    for d in part:
        res *= math.comb(s, d)
        s -= d
    return res
        
partitions = set()
FindPartition()
ans = 0

for part in partitions: 
    without_zero = math.comb(9, len(part))
    res = 1
    # How many ways can we pick the different numbers to have certain number of occurances
    n = len(part)
    for d in range(3,0,-1):
        k = len([i for i in part if i == d])
        res *= math.comb(n, k)
        n -= k
        
    ans += res * without_zero * Orderings(part)
    
    with_zero = math.comb(9, len(part)-1)
    res0 = 0
    # How many ways can we pick the different numbers to have certain number of occurances
    zeros = {}
    for d0 in range(3,0,-1):
        if d0 in part:
            n = len(part) - 1
            zeros[d0] = 1
            for d in range(3,0,-1):
                k = len([i for i in part if i == d])
                if d == d0:
                    k -= 1
                zeros[d0] *= math.comb(n, k)
                n -= k
    
    for n_zeros in zeros.keys():
        for i, d in enumerate(part):
            if d == n_zeros:
                new_part = part[:i] + (d-1,) + part[i+1:]
                # Orderings(new_part) many orderings start with a zero
                res0 += zeros[n_zeros] * (Orderings(part) - Orderings(new_part))
                break
            
    ans += res0 * with_zero