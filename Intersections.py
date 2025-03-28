from fractions import Fraction

limit = 5000
s = 290797
t = [[2*[0] for i in range(2)] for i in range(limit)]

for n in range(4 * limit):
    s = pow(s, 2, 50515093)
    line = n // 4
    number = n % 4
    t[line][number // 2][number % 2] = s % 500

def FindIntersectionPoint(L1, L2):
    x1, y1 = Fraction(L1[0][0]), Fraction(L1[0][1])
    x2, y2 = Fraction(L1[1][0]), Fraction(L1[1][1])
    x3, y3 = Fraction(L2[0][0]), Fraction(L2[0][1])
    x4, y4 = Fraction(L2[1][0]), Fraction(L2[1][1])

    if x1 == x2:  # L1 is vertical
        if x3 == x4:  # L2 is also vertical -> parallel, no intersection
            return None
        if x1 <= min(x3, x4) or x1 >= max(x3, x4):
            return None
        # Intersection with L2's line equation
        rc2 = (y4 - y3) / (x4 - x3)
        y = y3 + rc2 * (x1 - x3)
        if min(y1, y2) < y < max(y1, y2):
            return (x1, y)
        return None
    
    if x3 == x4:  # L2 is vertical
        if x3 <= min(x1, x2) or x3 >= max(x1, x2):
            return None
        rc1 = (y2 - y1) / (x2 - x1)
        y = y1 + rc1 * (x3 - x1)
        if min(y3, y4) < y < max(y3, y4):
            return (x3, y)
        return None
    
    # Slopes of the two lines
    rc1 = (y2 - y1) / (x2 - x1)
    rc2 = (y4 - y3) / (x4 - x3)

    if rc1 == rc2:  # Parallel lines
        return None
    
    # Intersection point x-coordinate
    x = (y3 - y1 + rc1 * x1 - rc2 * x3) / (rc1 - rc2)
    
    # Check if x is within both line segments
    if min(x1, x2) < x < max(x1, x2) and min(x3, x4) < x < max(x3, x4):
        y = y1 + rc1 * (x - x1)
        return (x, y)
    return None

TrueIntersectionPoints = set()

for i in range(limit):
    for j in range(i + 1, limit):
        intersection = FindIntersectionPoint(t[i], t[j])
        if intersection is not None:
            TrueIntersectionPoints.add(intersection)

print(len(TrueIntersectionPoints))
