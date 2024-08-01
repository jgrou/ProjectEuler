from sympy import divisors

limit = 10**8
ans = 0
half_limit = limit // 2

# First all real numbers
for a in range(1, int(limit**0.5)+1):
    ans += a                       # First add all the squares
    k = limit // a                 # For i between a+1 and k add both i and a: compute whole sum at once
    ans += a * (k - a)             # a
    ans += k*(k+1)//2 - a*(a+1)//2 # i

# Now all complex numbers
# For n to be divisible by a+bi, n*a and n*b should both be divisible by a**2 + b**2, 
# So a**2 + b**2 should divide n * gcd(a,b)
# First a=b
for a in range(1, half_limit + 1): 
    ans += 2 * a * (limit // (2*a)) # For i between 1 until limit/2a add both a+ai and a-ai

# Now b > a
for a in range(1, half_limit//2 + 1): 
    div = divisors(a)
    div.reverse()
    checked = set()
    
    for gcd in div:
        if limit * gcd < a**2:
            break
        max_b = int((limit * gcd - a**2)**0.5) # limit * gcd(a,b) > a^2 + b^2
        b = a + gcd
        
        while b <= max_b:
            if b not in checked:
                k = a**2 + b**2
                ans += 2 * (a+b) * int(limit*gcd/k) # For i between 1 until limit*gcd/k add a+bi, a-bi, b+ai, b-ai
                checked.add(b)
            b += gcd

print(ans)