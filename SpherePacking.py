from scipy.optimize import minimize

def lowest_sphere_position(x0, y0, z0, r0, r1, tube_radius=50):
    # Distance constraint: surface-to-surface contact
    contact_distance = r0 + r1

    def objective(p):
        # We want to minimize z1
        return p[2]

    def constraint_distance(p):
        # Keep the new sphere just touching the first one
        return (p[0] - x0)**2 + (p[1] - y0)**2 + (p[2] - z0)**2 - contact_distance**2

    def constraint_tube(p):
        # Ensure the new sphere is within the tube
        return (tube_radius - r1)**2 - (p[0]**2 + p[1]**2)

    def constraint_increasing(p):
        # Ensure the z-coordinate is increasing, since we also have the previous balls
        return p[2] - z0

    constraints = [
        {'type': 'eq', 'fun': constraint_distance},
        {'type': 'ineq', 'fun': constraint_tube},
        {'type': 'ineq', 'fun': constraint_increasing}]

    initial_guess = [-x0, -y0, z0 + contact_distance]
    result = minimize(objective, initial_guess, constraints=constraints)
    return result.x

# Basically all we have to determine is the order in which we drop the balls in the tube: n!/2 possibilities
# The best ordering found by brute-force for small numer of balls is:
# (max-1, max-3, ..., min, min+2, ..., n)

r = []
for radius in range(49, 29, -2):
    r.append(radius)

for radius in range(30, 51, 2):
    r.append(radius)

# First ball
x = (50 - r[0])/2**0.5
center = [(x,x,r[0])]

for i in range(len(r)-1):
    x1, y1, z1 = lowest_sphere_position(center[-1][0], center[-1][1], center[-1][2], r[i], r[i+1])
    center.append((x1,y1,z1))

ans = center[-1][2] + r[-1]
print(round(ans* 10**3))
