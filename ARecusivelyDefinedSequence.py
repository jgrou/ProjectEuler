import math

def f(x):
    return math.floor(2**(30.403243784 - x**2)) * 1e-9

n = 10**3

u = (n+1) *[-1]

for i in range(n):
    u[i+1] = f(u[i])