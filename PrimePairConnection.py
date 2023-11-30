from functools import reduce

def IsPrime(n):
    if n<2:
        return False
    for p in primes:
        if n%p == 0:
            return False
        if p > int(n**0.5):
            break
    return True

# Returns integer x that is a_i mod m_i for all i
def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m) # Calculate product of elements of m
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        _, r, s = ExtendEuclidanAlgorithm(n_i, p)
        sum += a_i * s * p
    return sum % prod
 
# Calculate s, t and r such that a * s + b * t = gcd(a,b) = r
def ExtendEuclidanAlgorithm(a,b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r1, r0 = r0%r1, r1
        s1, s0 = s0 - q * s1, s1
        t1, t0 = t0 - q * t1, t1
    return r0, s0, t0

primes = []
p = 1
ans = 0

while p <= 1_000_000:
    p += 1
    if IsPrime(p):
        primes.append(p)

# Add one more prime, since we need one p2 above 1_000_000
while True:
    p += 1
    if IsPrime(p):
        primes.append(p)
        break
    
for i in range(2, len(primes)-1):
    p1 = primes[i]
    p2 = primes[i+1]
    step = 10**len(str(p1)) # Iterate over all number with last two digits p1
    S = chinese_remainder([p2, step], [0,p1])
    ans += S