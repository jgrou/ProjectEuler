limit = 12
x0 = 1
x1 = 17
ans = 17

for _ in range(limit-1):
    x1, x0 = x1 * 18 - x0, x1
    ans += x1