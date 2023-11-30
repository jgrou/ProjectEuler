n = 1
ans = 0

while len(str(9**n)) == n:
    number = 0
    for k in range(1,10):
        number = k**n
        if len(str(number)) == n:
            ans += 1
    n += 1