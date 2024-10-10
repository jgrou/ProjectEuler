from scipy import integrate

limit = 10**5
ans = 0

# s = (k * a + 1)**2 + (k * b + 1 )**2 = k**2 * (a**2 + b**2) + 2 *k * (a + b) + 2
# s > (k-0.5)**2 = k**2 - k + 0.25 and s < (k+0.5)**2 = k**2 + k + 0.25
# k**2 * (a**2 + b**2 - 1) + k * (2a+2b+1) + 1.75 > 0 > k**2 * (a**2 + b**2 - 1) + k * (2a+2b-1) + 1.75
# The probability is the surface of values a and b within the square [0,1]x[0,1] that satisfies these values

for k in range(1, limit + 1):
    def P(a):
        a1 = k**2
        b1 = 2*k
        c1 = k**2 * (a**2 - 1) + k * (2*a - 1) + 7/4
        D1 = b1**2 - 4 * a1 * c1
        b_max = (-b1 + D1**0.5) / (2*a1) # This is trivially smaller than 1
        
        c2 = k**2 * (a**2 - 1) + k * (2*a + 1) + 7/4 # c2 > c1
        D2 = b1**2 - 4 * a1 * c2  # a1>0, so D2 < D1
        
        if D2 < 0:
            b_min = 0 # If the value is complex, if holds for any b
        else:
            b_min = max((-b1 + D2**0.5) / (2*a1), 0.0) # b_min < b_max
        
        return b_max - b_min
  
    a_max = min((-2 + (-3 + 4*k**2 + 4*k)**0.5) / (2*k), 1.0) # D1 > 0, b_max > 0
    #print(a_max)
    p = integrate.quad(P, 0.0, a_max, epsabs=4e-15, epsrel=0.0)[0]
    ans += p * k # Total error < 1e-5 -> error in p*k < 1e-10 -> error in p < 1e-15
    
print(round(ans,5))