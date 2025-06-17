# For the first one we need m+n-2 moves
# After that 3 moves to alternate bewteen going right or down: 2*(min(m,n)-1) times
# Or if m==n, 2*(m-1) - 1 times
# After that 5 moves to perform the same direction twice: abs(m-n) - 1 times
import math

limit = 10**6

IsPrime = (limit+1) * [True]
for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit, p):
            IsPrime[k] = False

ans = 0

for p in range(2, limit):
    if IsPrime[p]:
        # If m=n: p**2 = 8m - 11
        if (p**2 + 11)%8 == 0:
            ans += 1
        # If m!=n. Suppose m>n: p**2 = 6m + 2n - 13
        # 2n = p**2 - 6m + 13, p is always odd, so p**2 - 6m + 13 is always even
        # 2m > p**2 - 6m + 13
        # 8*m > p**2 + 13
        # m > (p**2 + 13)/8
        # p**2 - 6m + 13 >= 4
        # 6m <= p**2 + 9
        # m <= (p**2 + 9)/6
        min_m = math.ceil((p**2 + 13)/8)
        max_m = int((p**2 + 9)/6)
        ans += 2 * (max_m + 1 - min_m)

print(ans)
