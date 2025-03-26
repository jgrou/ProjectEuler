LIMIT = 120_000
d = set()

for p in range(1, LIMIT-1):
    for q in range(1, LIMIT - p):
        # The angles CTB, CTA and BTA are all 120 degrees
        a_sq = p**2 + q**2 + p * q
        a = round(a_sq**0.5)
        if a**2 == a_sq:
            for r in range(1, LIMIT - p - q + 1):
                c_sq = q**2 + r**2 + q * r
                b_sq = p**2 + r**2 + p * r
            
                c = round(c_sq**0.5)
                b = round(b_sq**0.5)

                if c**2 == c_sq and b**2 == b_sq:
                    if c_sq < a_sq + b_sq + a * b:  # Angle below 120 degrees
                        d.add(p+q+r)
                    
print(sum(d))
# 19054130, but not correct
