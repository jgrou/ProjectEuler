import math
from scipy import integrate

# Suppose every circle has radius 1 and the left bottom is (0,0)
L = 1 - math.pi / 4 # The area of the L section 
# The formula of the line is y = x/n
# The formula of the first circle is (x-1)^2 + (y-1)^2 = 1
n = 1
percentage = 50

while percentage > 0.1:
    n += 1
    x = (1 + 1/n - (2/n)**0.5) / (1 + 1/n**2)
    y = x / n
    area = 0.5 * x * y
    area += integrate.quad(lambda t: 1 - (2 * t - t**2)**0.5, x, 1.0)[0]
    percentage = area / L * 100