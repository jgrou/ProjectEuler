# The marsh is at 45 degrees with AB
# If we go in a straight line to B, the distance until the marsh is 50-25*sqrt(2)
# So the shortest path to the marsh is x1 = 25 * (sqrt(2) - 1)
# There are 7 angles to find: theta1, theta2,..., theta6
# Then the last angle is fixed, so that we get back to B
# The length of the path until the marsh is x1 / cos(theta1)
# The next five lengths are 1/cos(thetai)
# The time is distance/speed
import math
from scipy.optimize import minimize

v = [10,9,8,7,6,5,10]
x1 = 25 * (math.sqrt(2) - 1)
x = [x1,10,10,10,10,10,x1]

def time(theta):
    res = 0
    h = 0
    for i in range(6):
        L = x[i] / math.cos(theta[i])
        h += L * math.sin(math.pi/4 - theta[i])
        res += L / v[i]
    diag = h * math.sqrt(2) # / math.sin(math.pi/4)
    L_end = ((diag + x1)**2 + x1**2)**0.5
    res += L_end / v[6]
    return res

theta = [math.pi/4] * 6
bounds = [(0, math.pi/3)] * 6
result = minimize(time, theta, bounds=bounds, tol=1e-10)
ans = result.fun
print(round(ans,10))
