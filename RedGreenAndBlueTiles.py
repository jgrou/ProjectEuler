N = 50
F = [0,1,2,4,8]
for n in range(5,N+1):
    F.append(F[n-1] + F[n-2] + F[n-3] + F[n-4])
