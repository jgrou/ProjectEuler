limit = 100_000

# Cardano finds that t**3 + p*t + q = 0 has solutions
# cbrt(a + b * c**0.5) + cbrt(a - b * c**0.5)
# with a = -q/2, b = 1 and c = q**2/4 + p**3/27
# This is 1, if 1+p+q=0

# max_c = (6*limit/7)**2 // 4 + (6*limit/7)**3 // 27 = 31043733718658879514091

ans = 0

for i,p in enumerate(range(3, int(6*limit/7), 6)): # q divisible by 2 and p divisible by 3; worst case: c=b
    q = -1 - p
    a = -q//2
    c = q**2 // 4 + p**3 // 27
    
    # If c is the multiple of a square, we can mulitply b with the root and divide c by the square
    min_b = max(1,int(((2 * c) / (2 * limit - 3 - p))**0.5)) # Minimal b s.t. a+b+c <= limit
    max_b = limit - a - 1
    max_b = min(int((c/2)**0.5), max_b)
    #lst = []
    #lst2 = []
    
    for b in range(min_b, max_b + 1):
        square = b**2
        if c%square == 0:
            new_c = c // square
            
            #lst2.append(b)
            if a + b + new_c <= limit:
             #   lst.append(b)
                ans += 1
            
    #print(p, lst2, lst)
    
print(ans)