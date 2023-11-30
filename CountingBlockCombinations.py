m = 50
F = [1] * m

n = m - 1

while F[-1] < 1e6:
    n += 1
    F.append(F[n-1] + 1)
    for k in range(0,n-m):
        F[n] += F[k]