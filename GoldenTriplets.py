import fractions
import math

def f(x,y,z,n):
    return (x**n + y**n - z**n) * (x+y+z)

# By Fermat's last theorem this does not have any solutions for integer x,y,z for n>2.
order = 35
s = set()

for bx in range(2, order+1):
    for ax in range(1,bx):
        if math.gcd(ax,bx) > 1:
            continue
        x = fractions.Fraction(ax,bx)
        for by in range(2,order+1):
            for ay in range(1,by):
                if math.gcd(ay,by) > 1:
                    continue
                y = fractions.Fraction(ay,by)
                if y > x: # x and y are interchangable
                    continue
                for bz in range(2,order+1):
                    for az in range(1,bz):
                        if math.gcd(bz,az) > 1:
                            continue
                        z = fractions.Fraction(az,bz)
                        if f(x,y,z,1) == 0 or f(x,y,z,2) == 0 or f(x,y,z,-1) == 0 or f(x,y,z,-2) == 0:
                            s.add(x+y+z)

t = sum(s)
ans = t.numerator + t.denominator
print(ans)
