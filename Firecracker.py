import math

h = 100
v = 20
g = 9.81

max_heigth = 100 + v**2 / (2  * g)
factor = g / (2 * v**2)

V = 0.5 * math.pi * max_heigth**2  / factor

print(round(V,4))
