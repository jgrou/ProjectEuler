m = 100
ans = 0
N_points = {}

for a in range(1, m + 1):
    for b in range(1, a + 1):
        n_points = 0
        for x in range(1,a):
            if (b*x) % a == 0:
                n_points += (b - b*x//a - 1)  # Strictly contain
            else: 
                n_points += int(b - b*x/a) 
                
        N_points[(a,b)] = n_points
        N_points[(b,a)] = n_points
                
for a in range(1, m + 1):
    for b in range(1, m + 1):                
        for c in range(1, m + 1):
            for d in range(1, b + 1):
                LatticePoints = a + b + c + d + N_points[(a,b)] + N_points[(b,c)] + N_points[(c,d)] + N_points[(d,a)] - 3
                    
                if round(LatticePoints**0.5)**2 == LatticePoints:
                    if b == d:
                        ans += 1
                    else:
                        ans += 2