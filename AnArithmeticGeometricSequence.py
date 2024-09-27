def s(n,r):
    return 900 * (1 - r**n) / (1 - r) - 3 * (n * r**n * (r-1) - r**n + 1) / (1-r)**2

def f(r):
    return s(5000, r)

limit = -600_000_000_000

left = 1.001
right = 1.01

while right - left > 1e-12:
    middle = (left + right) / 2
    if f(middle) > limit:
        left = middle
    else:
        right = middle