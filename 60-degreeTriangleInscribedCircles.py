# Let the angle between a and c be 60 degrees with a the longer side
n = 100
ans = int(100 * 12**0.5) # Equal-sided triangles

# a > b > c
for a in range(1, 2*n**2+1):
    # r^2 > a*c*(2*c-a)/(4*(2*a+c))
    c_max = ((4 * n**2 + a**2) + ((4 * n**2 + a**2)**2 + 64 * a**2 * n**2)**0.5) / (4 * a)
    for c in range(1, min(a-2, int(c_max))+1):
        b_sq = c**2 + a**2 - c*a
        b = int(b_sq**0.5)
        if b**2 == b_sq:
            s = (a + c + b) / 2
            r = ((s - a) * (s - c) * (s - b) / s)**0.5
            if r <= n:
                ans += 1
                #print(a,b,c,r)