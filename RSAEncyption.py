import math

p = 1009
q = 3643
phi = (p - 1) * (q - 1)      
E = {}
minimum = p * q
ans = 0

for e in range(2, phi):
    if math.gcd(e, phi) == 1:
        E[e] = (1 + math.gcd(e-1, p-1)) * (1 + math.gcd(e-1, q-1))  # Formula from math exchange
        if E[e] < minimum:
            minimum = E[e]

for key, value in E.items():
    if value == minimum:
        ans += key