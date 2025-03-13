from sympy import isprime
limit = 50_000_000
count = sum(1 for n in range(1, limit+1) if isprime(2 * n**2 - 1))
print(count)