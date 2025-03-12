limit = 10**12
strong_repunits = {1}

# Everyting is a repunit in base n-1: 11
for base in range(2, int(limit**0.5)+1):
    strong_repunit = base**2 + base + 1 # 111 in this base
    power = 3
    while strong_repunit < limit:
        strong_repunits.add(strong_repunit)
        strong_repunit += base**power
        power += 1
        
ans = sum(strong_repunits)