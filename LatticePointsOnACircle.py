# We are on the circle if the distance from (N/2,N/2) is N/sqrt(2)
# So (a,b) s.t. (N/2 - a)**2 + (N/2 - b**2) = N**2 / 2
# a**2 + b**2 = (a+b)*N

def g(N):
    ans = 0
    for a in range(1, N//2 + 1):
        b = (N - (N**2 - 4 * (a**2 - a * N))**0.5) / 2
        if int(b) == b:
            ans += 1
    return ans

def f(N):
    return 8 * g(N) + 4
    
# f(N) = 420 iff g(N) = 52
# If p and q are two prime f(p*q) = f(p) * f(q) / 4 or g(pq) = 2g(p)g(q) + g(p) + g(q)
# g(p**n) = n *g(p)
       
# It appears as if g(p) is either 0 or 1
# g(p**52) >= g(5**52), but 5**52 > 10**1
# g(pq) = 52, then (g(p),g(q)) = (1,17), (2,10), (3,7)
# 5**17 > 10**1
# g(pq) = 17, then (g(p), g(q)) = (3,2)
# g(pq) = 10, then (g(p), g(q)) = (3,1)
# g(pq) =  7, then (g(p), g(q)) = (2,1)
# So g(N) = 52 if
# N = p1**1 * p2 **2 * p3**3 (* k) 
# N = p1**10 * p2**2 (* k), this one gives trouble when testing
# N = p1**7 + p2**3 (* k)
# With pi's and k (prime) numbers such that g(k) = 0 and g(pi) = 1
# Smallest two primes are 5 and 13 so largest possible prime is 4733727

def sieve_of_eratosthenes(n):
    """Returns a list of all prime numbers up to n."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers

primes = sieve_of_eratosthenes(4733727)
prime_values = {}
primes_one = []

for p in primes:
    if p%4 == 1: # It appears as g(p) = 1 iff p%4 = 1
        prime_values[p] = 1
        primes_one.append(p)
    else:
        prime_values[p] = 0
        
def DivisbleByPrimesOne(m):
    '''Check if m can be dvided by a number in primes_one'''
    # smallest_k = 5**3 * 13**2 * 17
    # 10**11 // smallest_k < primes_one[-1]
    for p in primes_one:
        if p > m:
            return False
        if m%p == 0:
            return True
    
answer = 0

# First p1 * p2**2 * p3**3
for p3 in primes_one:
    if p3 > 675:
        break
    for p2 in primes_one:
        if p2 > (10**11 / (5 * p3**3))**0.5:
            break
        if p2 != p3:
            for p1 in primes_one:
                if p1 > (10**11 / (p2**2 * p3**3)):
                    break
                if p1 != p2 and p1 != p3:
                    # f(k) = 420, also all multiples of k except of numbers which are divisible by a number in primes_one
                    k = p1 * p2**2 * p3**3
                    n = 10**11 // k # Number of times k fits in 10**11
                    
                    for m in range(1, n+1):
                        if not DivisbleByPrimesOne(m):
                            answer += m*k
                            
# p1**10 * p2**2
for p2 in primes_one[1:]:
    if p2 > 101:
        break
    k = 5**10 * p2**2
    n = 10**11 // k # Number of times k fits in 10**11
    
    for m in range(1, n+1):
        if not DivisbleByPrimesOne(m):
            answer += m*k
    
# p1**7 * p2**3
for p1 in primes_one:
    if p1 > 18:
        break
    for p2 in primes_one:
        if p2 > (10**11 / p1**7)**(1/3):
            break
        if p2 != p1:
            k = p1**7 * p2**3
            n = 10**11 // k # Number of times k fits in 10**11
            
            for m in range(1, n+1):
                if not DivisbleByPrimesOne(m):
                    answer += m*k