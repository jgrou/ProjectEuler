def drs(x):
  if x == 0:
    return 0
  return ((x - 1) % 9) + 1

n = 999_999
DRS = [drs(x) for x in range(0, n + 1)]

for a in range(2, n):
    da = DRS[a]
    for b in range(2, 1 + (n // a)):
        ab = a * b
        if ab > n:
            break
        else:
            x = da + DRS[b]
            if DRS[ab] < x:
                DRS[ab] = x
    
ans = sum(DRS[2:])