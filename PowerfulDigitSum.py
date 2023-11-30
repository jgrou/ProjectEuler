ans = 0

for a in range(100):
    for b in range(100):
        n = str(a**b)
        DigitalSum = 0
        for i in range(len(n)):
            DigitalSum += int(n[i])
        if DigitalSum > ans:
            ans = DigitalSum