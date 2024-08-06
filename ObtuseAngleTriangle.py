import math
import matplotlib.pyplot as plt

# Lattice points on circle: https://oeis.org/A046109
# Lattice points on/inside circle: https://oeis.org/A049740
def g(N):
    ans = 0
    for a in range(1, N//2 + 1):
        b = (N - (N**2 - 4 * (a**2 - a * N))**0.5) / 2
        if int(b) == b:
            ans += 1
    return ans

def LatticePointsOnCircle(N):
    return 8 * g(N) + 4

def LatticePointsWithinRadius(r):
    res = 4*math.ceil(r)-3 # The lines
    for x in range(1, math.ceil(r)):
        for y in range(1, math.ceil(r)):
            if x**2 + y**2 < round(r**2,3):
                res += 4
            else:
                break # To make it a bit faster: we do not need tot check even bigger y
    return res

def LatticePointsWithinCircle(M, r):
    res = 0
    for x in range(math.floor(M[0] - r), math.ceil(M[0]+r)+1):
        for y in range(math.floor(M[1] - r), math.ceil(M[1]+r)+1):
            if (x - M[0])**2 + (y - M[1])**2 < round(r**2,3):
                res += 1
    return res

def N(r):
    C = (r//4, r//4)
    S = set()
    Obtuse = set()
    res = 0
    
    for x in range(r+1):
        for y in range(x, r+1-x):
            if x==y: # y cannot be equal to x otherwise, we have a line instead of a triangle
                S.add((-x,y))
                S.add((x, -y)) 
            else:
                S.add((x,y))
                S.add((-x,y))
                S.add((x,-y))
                S.add((-x,-y))
                
                S.add((y,x))
                S.add((-y,x))
                S.add((y,-x))
                S.add((-y,-x))
    
    for B in S:
        l1 = B[0]**2 + B[1]**2
        l2 = C[0]**2 + C[1]**2
        l3 = (B[0] - C[0])**2 + (B[1] - C[1])**2
        
        if 2*max(l1,l2,l3) > l1 + l2 + l3:
            res += 1
            Obtuse.add(B)
            
    return res, Obtuse

def N2(r):
    res = (r+1)**2 + r**2 # Total number of points in S
    res -= (r+1) # x=y
    res -= (r//4 + 1) * (r + 1) + r//4 * r # Strip from O to C
    res += LatticePointsWithinCircle((r/8,r/8), r/32**0.5) + 2 # Circle around O and C
    return res

def N3(r):
    # https://oeis.org/A066644
    return 2 * int(4 * math.pi * (r//4)**2)

def N4(r):
    return 25 * (r//4)**2 + (r//4) - 2 

def Plot(data): 
    x_coords = [x for x, y in data]
    y_coords = [y for x, y in data]
    plt.figure(figsize=(10,10))
    plt.scatter(x_coords, y_coords)
    plt.plot([0,R,0,-R,0],[-R,0,R,0,-R], color='r')
    plt.plot([R//2,3*R//4,-R//4,-R//2,R//2],[-R//2,-R//4,3*R//4,R//2,-R//2], color='r')
    plt.plot([-R//2,R//2],[-R//2,R//2], color='r')
    plt.plot([0,R//4,R//4,0,0], [0,0,R//4,R//4,0], color='r')
    #plt.xlim(-1,R//4+1)
    #plt.ylim(-1,R//4+1)
    plt.show()

for R in range(4,100,4):
    x,y = N(R)
    z = N2(R)
    a = LatticePointsWithinCircle((R/8,R/8), R/32**0.5)
    b = LatticePointsWithinRadius(R/32**0.5)
    print(x,z,a,b)