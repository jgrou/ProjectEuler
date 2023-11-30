ans = 0
den = 2
num = 3

for _ in range(1000):
    den, num = (den + num, 2 * den + num)
    if len(str(num)) > len(str(den)):
        ans += 1