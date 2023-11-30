N = 10000
d = N * [None]

for n in range(1,N):
    SumOfDivisors = 0
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            SumOfDivisors += i
    d[n] = SumOfDivisors
    
SumOfAmicableNumbers = 0

for n in range(1,N):
    if d[n] < N:
        if d[d[n]] == n and d[n] != n:
            SumOfAmicableNumbers += n