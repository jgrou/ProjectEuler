import math

def LatticePointsWithinRadius(n):
    '''Lattice points within the circle with radius (0,0) to (n,n)'''
    res = (2*n+1)**2 - 4 # The square through (n,n) minus the four corners
    x = n + 1
    while x < 2**0.5 * n:
        res += 4 # y=0
        max_y = (2 * n**2 - x**2)**0.5
        res += 8 * (math.ceil(max_y) - 1) # y from 1 to max_y
        x += 1
    return res

def N(r):
    res = (r+1)**2 + r**2 # Total number of points in S
    res -= (r+1) # x=y
    res -= (r//4 + 1) * (r + 1) + r//4 * r # Strip from O to C
    # Circle around O and C is the same as circle with center (0,0) and half radius. Only works if r is divisible by 8
    res += LatticePointsWithinRadius(r//8) + 2
    return res

print(N(1_000_000_000))