import math
limit = 25_000
ans = (limit - 1) // 2 # b=c, a=1

max_c = limit // 2 # a + b >=c

for c in range(1, max_c + 1):
    min_b = ((c**2 +1)/2)**0.5 # b >= a
    
    for b in range(math.ceil(min_b), c):
        a = round((c**2 - b**2 + 1)**0.5)
        if a**2 + b**2 == c**2 + 1:
            if a + b + c <= limit:
                #print(a,b,c)
                ans += 1