def DigitalSum(n):
    p = 0
    r = 0
    c = n
    Sum = 0
    for i in range(100):
        x = 9
        y = x * (20 * p + x)
        while y > c:
            x -= 1
            y = x * (20 * p + x)
            
        p = 10 * p + x
        r = c - y
        c = 100 * r
        Sum += x
        
    return Sum

ans = 0

for k in range(1, 101):
    if k**0.5 % 1 != 0:
        ans += DigitalSum(k)