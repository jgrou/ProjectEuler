import math

n = 100
N = str(math.factorial(n))
ans = 0

for i in range(len(N)):
    ans += int(N[i])