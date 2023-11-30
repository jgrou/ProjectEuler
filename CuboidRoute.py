def function(NoOfCuboids):
    ans = 0
    l = 1
    while True:
        for bh in range(1, 2*l+1):
            d = (l**2 + bh**2)**0.5
            if d%1 == 0:
                if bh <= l:
                    ans += int(bh / 2)
                else:
                    ans += int(l + 1 - bh / 2)
                if ans > NoOfCuboids:
                    return l
        l += 1 
        
ans = function(1_000_000)