limit = 10_000

def SquareDivisors(n, min_d = 1, max_d=None):
    if max_d is None:
        max_d = int((n/2)**0.5)
    else:
        max_d = min(int((n/2)**0.5), max_d)
        
    for i in range(min_d, max_d + 1):
        square = i**2
        if n%square==0:
            yield square
    root = int(n**0.5)
    if root**2 == n:
        yield n
        
# Cardano finds that t**3 + p*t + q = 0 has solutions
# cbrt(a + b * c**0.5) + cbrt(a - b * c**0.5)
# with a = -q/2, b = 1 and c = q**2/4 + p**3/27
# This is 1, if 1+p+q=0

max_c = (6*limit/7)**2 // 4 + (6*limit/7)**3 // 27 # 31043733718658879514091

ans = 0

for i,p in enumerate(range(3, int(6*limit/7), 6)): # q divisible by 2 and p divisible by 3; worst case: c=b
    q = -1 - p
    a = -q//2
    c = q**2 // 4 + p**3 // 27
    
    # If c is the multiple of a square, we can mulitply b with the root and divide c by the square
    min_d = ((2 * c) / (2 * limit - 3 - p))**0.5 # Minimal d s.t. a+b+c <= limit
    max_d = limit - a - 1
    lst = []
    lst2 = []
    
    for d in list(SquareDivisors(c, max(1,int(min_d)), max_d)):
        b = int(d**0.5)
        new_c = c // d
        lst2.append(b)
        if a + b + new_c <= limit:
            lst.append(b)
            ans += 1
            
    print(p, lst2, lst)
    
print(ans)