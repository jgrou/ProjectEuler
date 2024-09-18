# Pattern: slide, 1 hop, slide, 2 hops, slide, ..., slide, n hops, slide, n-1 hops, slide, ..., slide, 1 hop, slide

limit = 40
s = 0
ans = 0
n = 1

while s < limit:
    M = n**2 + 2*n
    k = (-1 + (1 + 8 * M)**0.5) / 2
    k = round(k)
    if k**2 + k == 2 * M:
        s += 1
        ans += n
    n += 1