import math

limit = 10**8
ans = 0
half_limit = limit // 2

def greatest_divisor(n):
    if n % 2 == 0:
        return n // 2
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return n // i
    return 1

# First all real numbers
for a in range(1, int(limit**0.5)+1):
    ans += a                     # First add all the squares
    k = limit // a             # For i between a+1 and k add both i and a: compute whole sum at once
    ans += a * (k - a)           # a
    ans += k*(k+1)/2 - a*(a+1)/2 # i

# Now all complex numbers
# For n to be divisible by a+bi, n*a and n*b should both be divisible by a**2 + b**2, 
# So a**2 + b**2 should divide n * gcd(a,b)
for a in range(1, half_limit + 1): 
    # First a=b
    ans += 2 * a * (limit // (2*a)) # For i between 1 until limit/2a add both a+ai and a-ai

    # Now b > a
    p = greatest_divisor(a)
    a_sq = a**2
    
    if limit * p > 2 * a_sq:
        upper_bound = int(min((limit * p - a_sq)**0.5, half_limit)) # limit * gcd(a,b) > a^2 + b^2 and gcd(a,b) < p, unless a divides b

        for b in range(a+1, upper_bound+1):
            gcd = math.gcd(a,b)
            k = a_sq + b**2
            ans += 2 * (a+b) * int(limit*gcd/k) # For i between 1 until limit*gcd/k add a+bi, a-bi, b+ai, b-ai

        lower_bound = upper_bound // a * a + a # The first multiple of a after upper_bound
    else:
        lower_bound = 2*a
    
    # Check for all b which are a mulitple of a, then gcd(a,b) = a
    uppest_bound = int(min((limit * a - a_sq)**0.5, half_limit))
        
    for b in range(int(lower_bound), uppest_bound+1, a):
        k = a_sq + b**2
        ans += 2 * (a+b) * int(limit*a/k) # For i between 1 until limit*gcd/k add a+bi, a-bi, b+ai, b-ai
    
print(ans)