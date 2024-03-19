for a in range(500):
    for b in range(500):
        c = (a**2 + b**2)**0.5
        if a+b+c == 1000:
            ans = a*b*c
