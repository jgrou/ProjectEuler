limit = 100_000_000

Phi = [n for n in range(limit+1)]
IsPrime = (limit + 1) * [True]

for p in range(2, limit+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
    
        for k in range(p, limit+1, p):
            Phi[k] *= (1 - 1/p)

ans = limit * (limit + 1) // 2
ans -= sum(Phi)#
    
ans *= 6
print(int(ans))