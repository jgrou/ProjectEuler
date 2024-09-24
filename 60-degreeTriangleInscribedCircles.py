from math import gcd
from scipy import optimize

limit = 1053779
ans = 0 

# Maybe we need to divide a,b,, by 3 so divide by 36 instead of 4
def R_sq(m,n):
    return (m*n + n**2) * (2 * m**2 + n**2 - 3*m*n) * (3*m*n - 3*n**2) / 36 / (2*m**2 + m * n - n**2)

# The largest possible value of m below the limit, is for n=1
def max_r(m):
    return R_sq(m,1) - limit**2

sol = optimize.root_scalar(max_r, x0=limit**2, method='newton')
max_M = int(sol.root)

for m in range(2,max_M+1):
    mod3 = m%3 # if m = -n mod 3, then gcd(a,b,c) = 3
    
    for n in range(1, m//2 + 1): #,duplicates can be avoided by going only till m/2
        if gcd(m, n) == 1 and (m+n)%3 !=0:
            a = m**2 + n**2 - m*n
            b = 2*m*n - n**2
            c = m**2 - n**2
            
            if a == b: # Equal-sided triangles are not allowed
                continue
            
            s = (a + c + b) / 2
            r = ((s - a) * (s - c) * (s - b) / s)**0.5
            
            if r > limit: # Increasing in n
                break  
            
            ans += int(limit/r)
    
    if mod3 != 0: # gcd(m,n) = 1
        for n in range(3 - mod3, m//2 + 1, 3): # m = -n mod 3
            if gcd(m, n) == 1:
                a = (m**2 + n**2 - m*n) // 3 # gcd(a,b,c) = 3
                b = (2*m*n - n**2) // 3
                c = (m**2 - n**2) // 3
            
                if a == b: # Equal-sided triangles are not allowed
                    continue

                s = (a + c + b) / 2
                r = ((s - a) * (s - c) * (s - b) / s)**0.5
            
                if r > limit: # Increasing in n
                    break  
            
                ans += int(limit/r)