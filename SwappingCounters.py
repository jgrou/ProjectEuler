# Pattern: slide, 1 hop, slide, 2 hops, slide, ..., slide, n hops, slide, n-1 hops, slide, ..., slide, 1 hop, slide
# M(n) = n**2 + 2*n = k**2 + k for some k
# For the correct n, n+1 follows A006452: a(n) = 6*a(n-2) - a(n-4), with the first four: 1,1,2,4

limit = 40

a = (limit + 2) * [1]
a[2] = 2
a[3] = 4

for n in range(4, limit+2):
    a[n] = 6 * a[n-2] - a[n-4]
    
ans = sum(a[2:]) - limit