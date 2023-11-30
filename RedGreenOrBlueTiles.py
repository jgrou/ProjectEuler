def CountingBlockCombinations(n,m):
    F = [0] * m
    for k in range(m,n+1):
        F.append(F[k-1] + F[k-m] + 1)
    return F[-1]

N = 50
ans = CountingBlockCombinations(N, 2) + CountingBlockCombinations(N, 3) + CountingBlockCombinations(N, 4)