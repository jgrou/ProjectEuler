import math

N = 50_000_000
values = N * [0]
ans = 0

for z in range(1, int(1.5*N)):
    min_diff = math.ceil(z/3)
    max_diff = math.floor( (-2*z + (16 * z**2 + 12 * N)**0.5) / 6 )
    
    for diff in range(min_diff, max_diff + 1):
        y = z + diff
        x = y + diff
        
        n = x**2 - y**2 - z**2
        values[n-1] += 1
        
for x in values:
    if x == 1:
        ans+= 1