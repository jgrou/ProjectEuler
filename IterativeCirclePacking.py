import math
iterations = 10

def r4(r1, r2, r3):
    '''Given the radii of three mutually tangent circles, return the radius of the fourth mutually tangent circle
    negative radius means this circle surrounds the other three'''
    a = 2 * (r1 + r2 + r3) - r1*r2/r3 - r1*r3/r2 - r2*r3/r1
    b = 2 * (r1*r2 + r1*r3 + r2*r3)
    c = -r1*r2*r3
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2 * a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2 * a)
    return min(abs(x1), abs(x2))

def gap(r1, r2, r3, depth=1):
    r = r4(r1, r2, r3)
    ans = math.pi * r**2
    if depth < iterations:
        ans += gap(r1,r2,r,depth+1)
        ans += gap(r1,r,r3,depth+1)
        ans += gap(r,r2,r3,depth+1)
    return ans

r_depth1 = (48**0.5 - 6) / 2 # The radius of first three circles
res = 3 * gap(r_depth1, r_depth1, -1) + gap(r_depth1, r_depth1, r_depth1)
fraction = round((math.pi - 3 * math.pi * r_depth1**2 - res) / math.pi, 8) # Assuming the outer circle has radius 1
