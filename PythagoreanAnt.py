from scipy.integrate import dblquad
import math

# Define the function to integrate
def LongSide(x, y):
    alpha = math.atan(y/(3-x))
    beta = math.atan(x/(4-y))
    return (math.pi/2 + alpha + beta) / (2*math.pi)

# x limits as a function of y
def x_lower(y):
    return 0

def x_upper(y):
    return 3 - 3*y/4

# y limits
y_lower = 0
y_upper = 4

# Compute the double integral
result, error = dblquad(LongSide, y_lower, y_upper, x_lower, x_upper)
print(round(result/6,10))  # Divide by 6 which is the area of the triangle
