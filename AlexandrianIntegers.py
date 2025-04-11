# We need two negatives and one positive, with the positive being the smallest
# https://oeis.org/A147811
limit = 150_000 

def Divisors_of(x):  # Find the first half of the divisors of a number
    divisors = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

A = []
p = 1
while len(A) < limit:
    n = p**2 + 1
    for k in Divisors_of(n):
        A.append(p * (p + k) * (n//k + p))
    p += 1

m = max(A)

while p <= (m*2/5)**(1/3):
    n = p**2 + 1
    for k in Divisors_of(n):
        A.append(p * (p + k) * (n//k + p))
    p += 1

A.sort()    
print(A[limit-1])
