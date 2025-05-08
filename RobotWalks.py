import math

# Every walk can be represented as a binary string of 1 for anti-clockwise and 0 for clockwise
# Represent every point as a point on the unit circle with center (x,y) and angle phi
# Remember dictionary with keys (x,y,phi,prev_bit) and how often every final position occurs
limit = 70
ans = 0
positions = {(0,0,0,1):1}

for steps in range(limit):
    new_positions = {}
    for (x,y,phi,prev_bit) in positions:
        for bit in [0,1]:
            if bit != prev_bit:
                new_x = round(x + 2*math.cos(phi*math.pi/180),8) # math uses radial
                new_y = round(y + 2*math.sin(phi*math.pi/180),8)
                new_phi = phi + 180
            else:
                new_x = x
                new_y = y
                new_phi = phi
        
            if bit == 0:
                new_phi -= 72
            elif bit == 1:
                new_phi += 72
            new_phi %= 360

            if (new_x, new_y, new_phi, bit) not in new_positions:
                new_positions[(new_x, new_y, new_phi, bit)] = positions[(x,y,phi,prev_bit)]
            else:
                new_positions[(new_x, new_y, new_phi, bit)] += positions[(x,y,phi,prev_bit)]
    positions = new_positions

ans = 2*positions[(0,0,0,1)]
print(ans)
