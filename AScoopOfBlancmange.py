from scipy import integrate, optimize
import numpy as np

def s(x):
    return abs(x - np.round(x))

def y(x):
    res = 0
    for n in range(100):
        res += s(2**n * x) / 2**n
    return res

def circle(x):
    return 0.5 - (0.5*x - x**2)**0.5

# find intersection
def f(x):
    return y(x) - circle(x)

sol = optimize.root(f, 0.1)
x1 = sol.x[0]
x2 = 0.5 # y(1/2) = 1/2 which is also on the circle

def I(x):
    # Integral of the curve according to wikipedia
    if x == 1.0:
        return 0.5
    if x <= 0.5:
        return I(2*x)/4 + x**2/2
    else:
        return 0.5 - I(1-x)

result1 = I(x2) - I(x1)
result2, error2 = integrate.quad(circle, x1, x2)
ans = result1 - result2
print(round(ans,8))

