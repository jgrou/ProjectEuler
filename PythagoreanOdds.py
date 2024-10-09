from scipy import integrate

limit = 10**5
ans = 0

# s = (k * a + 1)**2 + (k * b + 1 )**2 = k**2 * (a**2 + b**2) + 2 *k * (a + b) + 2
# s > (k-0.5)**2 = k**2 - k + 0.25 and s < (k+0.5)**2 = k**2 + k + 0.25
# k**2 * (a**2 + b**2 - 1) + k * (2a+2b+1) + 1.75 > 0 > k**2 * (a**2 + b**2 - 1) + k * (2a+2b-1) + 1.75

for k in range(1, limit + 1):
    def b_max(a):
        a1 = k**2
        b1 = 2*k
        c1 = k**2 * (a**2 - 1) + k * (2*a - 1) + 7/4
        D = b1**2 - 4 * a1 * c1
        if D < 0:
            return 0.0 # If the value is complex, there are no solutions for b
        else:
            return max(min((-b1 + D**0.5) / (2*a1), 1.0),0.0)

    def b_min(a):
        a1 = k**2
        b1 = 2*k
        c2 = k**2 * (a**2 - 1) + k * (2*a + 1) + 7/4
        D = b1**2 - 4 * a1 * c2
        if D < 0:
            return 0.0 # If the value is complex, if holds for any b
        else:
            return min(max((-b1 + D**0.5) / (2*a1), 0.0), 1.0)
        
    lower_integral = integrate.quad(b_min, 0.0, 1.0, epsabs=1e-10, epsrel=1e-11)[0]
    upper_integral = integrate.quad(b_max, 0.0, 1.0, epsabs=1e-10, epsrel=1e-11)[0]
    p = upper_integral - lower_integral
    
    ans += p * k
    
print(round(ans,5))