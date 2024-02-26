x = 1504170715041707
y = 4503599627370517
ans = 1504170715041707

# Use Extended Euclidean Algorithm
while x > 1:
    x, y = (y // x + 1) * x - y , x
    ans += x