import math

# You can form a lamina with x tiles if x = a**2 - b**2 for some a and b with the same parity
limit = 1_000_000
ans1 = 0 # Answer to problem 1
ans2 = 0 # Answer to problem 2

# Make a dictionary where the keys are the number of tiles and the value how many triangles can be formed
L = {}

for t in range(1, limit+1):
    L[t] = 0

# a**2 - (a - 2)**2 = 4a - 4 <= limit. So a <= limit/4 + 1
# a**2 - b**2 <= limit. So b**2 >= a**2 - limit

minimal_hole = 1

for a in range(3, limit//4 + 2):
    if a**2 > limit:
        minimal_hole = math.ceil((a**2 - limit)**0.5)
    for b in range(a-2, minimal_hole-1, -2):
        ans1 += 1
        
        t = a**2 - b**2
        L[t] += 1
        
for t in range(1, limit+1):
    if L[t] >0 and L[t] <= 10:
        ans2 += 1