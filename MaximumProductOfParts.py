import math

limit = 10000
ans = 0
IsPrime = (limit + 1) * [True]
for p in range(2, int(limit**0.5) + 1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False           
Primes = [3] + [p for p in range(7,limit+1,2) if IsPrime[p]]

def Terminating(N,k):
    # Non-terminating if there are other prime factors than 2 or 5 in the reduced denominator
    # To the power k does not matter
    for p in Primes:
        Np = 0
        kp = 0
        while N%p == 0:
            Np += 1
            N //= p
        while k%p == 0:
            kp += 1
            k //= p
        if kp > Np:
            return False
    return True

for N in range(5, limit+1):
    x = N / math.exp(1)  # The max of (N/k)^k is at N/exp(1)
    k1 = math.ceil(x)
    k2 = k1 - 1
    
    if k1 * math.log(N / k1) > k2 * math.log(N / k2):  # Real numbers are too large
        k = k1
    else:
        k = k2

    if Terminating(N,k):
        ans -= N
    else:
        ans += N