# a,b odd, then c odd
# a odd and b even, then c even
# a and b both even, then a**2 + b**2 is divisible by 4, which c**2 + 1 cannot be

# a**2 + b**2 = c**2 + 1
# c**2 - a**2 = b**2 - 1
# (c-a)*(c+a) = (b-1)*(b+1)
# (c+a)/(b+1) = (b-1)/(c-a) = m/n
# (b+1)/(c+a) = n/m
# c+a = k*m, b+1 = k*n, b-1 = i*m, c-a = i*n

#2b = k*n + i*m, both k*n and i*m even or both odd
#2a = k*m - i*n
#2c = k*m + i*n

import math
limit = 100
ans = (limit - 1) // 2 # b=c, a=1

max_c = limit // 2 # a + b >=c

for c in range(1, max_c + 1):
    c2_plus_1 = c**2 + 1
    min_b = math.ceil(((c2_plus_1)/2)**0.5) # b >= a

    if c&1: # If c is odd, then b must be odd
        if not min_b&1:
            min_b += 1
        step = 2
    else:
        step = 1
    
    for b in range(min_b, c, step):
        a2 = c2_plus_1 - b**2
        a = round(a2**0.5)
        if a**2 == a2:
            if a + b + c <= limit:
                ans += 1
                print(a,b,c)
