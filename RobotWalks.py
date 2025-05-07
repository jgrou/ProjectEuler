# Every walk can be represented as a binary string of 1 for anti-clockwise and 0 for clockwise
# mirroring or reversing should still work
# There must be a multiple of 5 steps left and right: but not all of these paths are valid.

# Swap from 1 to 0 or vice versa:
# new angle: = 180 + old_angle
# New center += (cos(phi) + sin(phi)

import math
import itertools
limit = 25
ans = 0

for n_zeros in range(0, limit//2, 5): # We can just swap all zeros and ones to obtain symmetric figure
    for zero_positions in itertools.combinations(range(limit), n_zeros):
        bits = [1] * limit
        for pos in zero_positions:
            bits[pos] = 0

        # Represent every point as a point on the unit circle with center (x,y) and angle phi
        x = 0
        y = 0     
        prev_bit = 1
        phi = 0
    
        for bit in bits:
            if bit != prev_bit:
                x += 2*math.cos(phi*math.pi/180) # math uses radial
                y += 2*math.sin(phi*math.pi/180)
                phi += 180
        
            if bit == 0:
                phi -= 72
            elif bit == 1:
                phi += 72
            phi %= 360
            prev_bit = bit

        final_x = x + math.cos(phi*math.pi/180)
        final_y = y + math.sin(phi*math.pi/180)

        if round(final_x, 8) == 1.0 and round(final_y,8) == 0.0:
            ans += 1

ans *=2
