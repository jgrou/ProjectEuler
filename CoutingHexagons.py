# https://oeis.org/A011779
limit = 12345

def T(n):
    return n*(n+1) // 2

def H(n):
    # Possible side lengths c
    # c**2 = a**2 + b**2 = 3/4 + (d+0.5)**2 = d**2 + d + 1
    res = 0
    multiplier = 1
    
    for d in range(3, n+1, 3):
        # Integer sided
        max_k = n//d - 1
        for k in range(max_k+1):
            res += multiplier * T(n - (d-1) - d*k)
        if d == 6: # Not symmetric anymore
            multiplier = 2
        
    return res

for n in range(15):
    print(n, H(n+3))