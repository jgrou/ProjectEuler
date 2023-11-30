import math

for a in range(500):
    for b in range(500):
        c = math.sqrt(a**2 + b**2)
        if a+b+c == 1000:
            ans = a*b*c