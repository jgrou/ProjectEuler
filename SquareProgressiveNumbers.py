limit = 10**12

# d = a * r / b; q = a^2 * r / b^2
# We can assume without loss of generality that a and b are
# relatively prime, so q can be an integer only if r is divisible by b^2.  So
# r = c*b^2, q = a*c*b, d = a^2*c
# n = dq+r = a^3*b*c^2 + c*b^2.

def gcd(a, b):
    while b: 
        a, b = b, a%b 
    return a
    
def issquare(n):
    x = int(n**0.5)
    return x**2 == n

s = set()

for a in range(2, int(limit**(1/3)) + 1):
    a3 = a**3
    sb = (a + 1) % 2 + 1 # If a is odd, this is 1, if even, this is 2: a,b are relatively prime
    
    for b in range(1, a, sb):
        n = b * (a3 + b)
        
        if n > limit:
            break
        if gcd(a, b) == 1:
            c = 1
            while n < limit:
                if issquare(n): 
                    s.add(n)
                c += 1
                n = b * c * (c * a3 + b)
            
print(sum(s))