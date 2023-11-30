import math

primes = []
x = 2

def Prime(n):
    if n <2:
        return False
    for p in primes:
        if p > math.sqrt(n):
            break
        if n%p == 0:
            return False
    return True

while sum(primes) < 10**6:
    if Prime(x):
        primes.append(x)
    x += 1

def main():
    for i in reversed(range(len(primes))):
        for j in range(len(primes)-i):    
            ans = sum(primes[j:i+j])
            if Prime(ans):
                return ans
            
answer = main()