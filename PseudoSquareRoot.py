import math

limit = 190
IsPrime = (limit+1)*[True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

Primes = [p for p in range(2, limit+1) if IsPrime[p]]
n = len(Primes)
p = 1

for k in Primes:
    p *= k

bound = math.isqrt(p)

# Every divisor of p is a combination of primes: so 2**n possibilities
m = n // 2
lower = set() # All possible products with lower half of prime numbers, 
upper = set() # All possbile products with upper half of prime numbers

def subsets(i=0, prod_l=1, prod_u=1):
    if i == m:
        lower.add(prod_l)
        if prod_u <= bound:
            upper.add(prod_u)
        return
    subsets(i+1, prod_l, prod_u)
    subsets(i+1, prod_l*Primes[i], prod_u*Primes[m+i])

subsets()

# For each lower value find the optimal upper_value: quickest if upper values are sorted
upper_keys = list(upper)
upper_keys.sort()

def find(key, lst):
    # Binary search
    lower = 0
    upper = len(lst) - 1

    while lower < upper:
        middle = (upper + lower) // 2
        
        if lst[middle] * key > bound:
            upper = middle - 1
        elif lst[middle+1] * key <= bound:
            lower = middle + 1
        else:
            return lst[middle]

    return lst[lower]

ans = 1

for lower_value in lower:
    upper_value = find(lower_value, upper_keys)
    ans = max(ans, lower_value * upper_value)

print(ans%10**16)
