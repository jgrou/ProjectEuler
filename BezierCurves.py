from scipy import integrate, optimize
import math

# y_Q0 = t*v
# x_Q0 = 1  
# x_Q1 = t*v + (1-t)
# y_Q1 = t + (1-t)*v   
# x_Q2 = (1-t)*v
# y_Q2 = 1   
# x_R0 = t*x_Q1 + (1-t)*x_Q0
# y_R0 = t*y_Q1 + (1-t)*y_Q0 
# x_R1 = t*x_Q2 + (1-t)*x_Q1
# y_R1 = t*y_Q2 + (1-t)*y_Q1
# x_B = t*x_R1 + (1-t)*x_R0
# y_B = t*y_R1 + (1-t)*y_R0

def integrand(t, v):
    y_B = 3 * t**2 + 3 * t * v - 6 * t**2 * v - 2 * t**3 + 3 * t**3 * v
    dx_B = 6 * t * v - 9 * t**2 * v - 6 * t + 6 * t**2
    return dx_B * y_B

def surface(v):
    return integrate.quad(integrand, 1, 0, args=(v,))[0]

def equation(v):
    return surface(v) - math.pi/4

v = optimize.root(equation, 0.5).x[0]

def f(t):
    dx_B = 6 * t * v - 9 * t**2 * v - 6 * t + 6*t**2
    dy_B = 6 * t + 3 * v - 12 * t * v - 6 * t**2 + 9 * t**2 * v
    return (dx_B**2 + dy_B**2)**0.5

L = integrate.quad(f, 0, 1)[0]
ans = 200 * (L - math.pi/2) / math.pi
print(round(ans,10))