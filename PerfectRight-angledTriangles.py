import math

limit = 10**16
# Suppose x**2 = c
# By Euclid's formula for generating Pythagorean triples: x**2 = m**2 + n**2
# So we can reapply Euclid's formula to find the triple x,m,n
limit_x = int(limit**0.5)

perfect = 0
super_perfect = 0

for y in range(1, int(limit_x**0.5) + 1):
    # If y is odd, then z is even and vice versa
    y_odd = y&1
    max_z = min(int((limit_x - y**2)**0.5), y-1)
    for z in range(1+y_odd, max_z+1, 2):
        if math.gcd(y, z) == 1:
            x = y**2 + z**2
            m = max(y**2 - z**2,  2 * y * z)
            n = min(y**2 - z**2,  2 * y * z)
            
            a = m**2 - n**2
            b = 2 * m * n
            c = x**2
            
            perfect += 1
            area = a*b // 2
            if area % 6 == 0 and area % 28 == 0:
                super_perfect += 1
                    
ans = perfect - super_perfect