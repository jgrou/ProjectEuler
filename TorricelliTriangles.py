LIMIT = 120_000
d = set()

for p in range(1, LIMIT):
    for q in range(p, LIMIT - p):
        a_sq = p**2 + q**2 + p * q
        a = round(a_sq**0.5)
        if a**2 == a_sq:
            for r in range(q, min(p + q, LIMIT - p - q + 1)):
                # calculate the distances from Torrirelli point
                c_sq = q**2 + r**2 + q * r
                b_sq = p**2 + r**2 + p * r
            
                c = round(c_sq**0.5)
                b = round(b_sq**0.5)

                if c**2 == c_sq and b**2 == b_sq:
                    d.add(p+q+r)
                    
print(sum(d))
# 19054130, but not correct
