n = 13
d = 1000
r = 0
p = 0
ans = -int(n**0.5)

for _ in range(d):
    x = 9
    y = x * (20*p+x)
    
    while y > n:
        x -= 1
        y = x * (20*p+x)

    ans += x
    p = 10*p + x
    r = n - y
    n = 100 * r