import math

r = 105
upper_points = []

for x in range(r):    
    max_y = math.ceil((r**2 - x**2)**0.5)
    for y in range(1, max_y):
        upper_points.append((x,y))
        if x != 0:
            upper_points.append((-x,y))

# Not all points can be on the same side of the x-axis
# Pick 2 points above x-axis and one point below
# If both lines cross the x-axis at the same side, 0 is not in the triangle
# This is equivalent to p1 * p2 >= 0 with
# p1 = (y1 * x3 - y3 * x1) / (y1 - y3)
# p2 = (y2 * x3 - y3 * x2) / (y2 - y3)
# y3 is the smallest y-value so we only need numerators of p1 and p2:
# For given y3 solve quadratic equation for x3 to obain bounds for x3

n_points = len(upper_points)
ans = 0

for i in range(n_points):
    for j in range(i+1, n_points):
        (x1,y1) = upper_points[i]
        (x2,y2) = upper_points[j]
        if x1*y2 == x2*y1: # If they are one a line with the origin, no possibilities
            continue
        for y3 in range(-1, -r ,- 1):
            max_x = math.ceil((r**2 - y3**2)**0.5) - 1
            p1 = y3*x1/y1
            p2 = y3*x2/y2
            left  = max(math.floor(min(p1,p2)) + 1, - max_x)
            right = min(math.ceil(max(p1,p2)) - 1, max_x)
            if right < -max_x or left > max_x:
                continue
            ans += 2 * (right-left+1) # Use symmetry, for two points below and one above

# Now with one point on the x-axis
for (x1,y1) in upper_points:
    for x2 in range(1,r): # Triangle with origin as corner, does not contain origin
        for y3 in range(-1, -r ,-1):
            max_x = math.ceil((r**2 - y3**2)**0.5) - 1
            p = y3 * x1 / y1
            ans += max(max_x - max(math.floor(p)+1,-max_x) + 1, 0) # For x2<0, x3 must be bigger than p
            ans += max(min(math.ceil(p)-1,max_x) + max_x + 1, 0)   # For x2>0, x3 must be smaller than p

print(ans)
