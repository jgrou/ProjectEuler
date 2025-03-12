import math

limit = 10**9
n = 100
numbers = set()
IsPrime = (n + 1) * [True]
for p in range(2, int(n**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, n+1, p):
            IsPrime[k]= False
Primes = [p for p in range(2,n+1) if IsPrime[p]]
max_index = len(Primes) - 1

def Hamming(index=0, current=1):
    p = Primes[index]
    max_power = int(math.log(limit/current, p))
    
    if index == max_index:
        for power in range(max_power+1):
            numbers.add(current * p**power)
    else: 
        for power in range(max_power+1):
            Hamming(index+1, current * p**power)
            
Hamming()
ans = len(numbers)