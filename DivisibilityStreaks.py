# An even number has streak = 1
# Streak at least 3, if n = 3k+1
# Streak at least 4, if n = 4k+1
# Streak at least 5, if n = 5k+1

import math

lcm = 33 * [1]
ans = 0

for s in range(1, 32):
    limit = 4**s
    lcm[s+1] = math.lcm(lcm[s], s+1)
    ans += (limit-2) // lcm[s] - (limit-2) // lcm[s+1]

print(ans)
