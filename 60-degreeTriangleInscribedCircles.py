# Let the angle A be 60 degrees
n = 100
ans = 0

# AB > BC > AC
# *2 *(2a - b) * a/ / (4*(a+2b)) <= n**2; a = AB, b = AC
for AB in range(1,2*n**2+1):
    for AC in range(1, AB):
        BC_sq = AC**2 + AB**2 - AC*AB # x_C = AC * 0.5, y_C = AC * 0.5 * 3**0.5
        BC = int(BC_sq**0.5)
        if BC**2 == BC_sq:
            s = (AB + AC + BC)/2
            r = ((s - AB) * (s - AC) * (s - BC) / s)**0.5
            if r<= n:
                ans += 1