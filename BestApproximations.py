# https://en.wikipedia.org/wiki/Simple_continued_fraction#Best_rational_approximations

def continued_fraction_sqrt(n):
    """Compute the continued fraction representation of sqrt(n)"""
    m = 0
    d = 1
    a0 = a = int(n**0.5)
    
    period = []
    seen = set()

    while (m, d, a) not in seen:
        seen.add((m, d, a))
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)

    return (a0, period[:-1])

def BestApproximation(n, d):
    a0, period = continued_fraction_sqrt(n)
    r_new, r = a0, 1
    s_new, s = 1, 0
    i = 0
    m = len(period)

    while s_new <= d:
        r_new, r, r_old = period[i] * r_new + r, r_new, r
        s_new, s, s_old = period[i] * s_new + s, s_new, s
        i += 1
        i%=m

    # Truncate the continued fraction, and reduce its last term by a chosen amount (possibly zero)
    a = period[i-1]
    even = not (a&1)
    half = (a+1) // 2

    while a > half: # The reduced term cannot have less than half its original value.
        a -= 1
        r_new = a * r + r_old
        s_new = a * s + s_old
        # If the final term is even, half its value is admissible only if the corresponding semiconvergent is
        # better than the previous convergent. 
        if a == half and even:
            if r_new * s > r * s_new:
                if n * (2 * s * s_new)**2 <= (r_new * s + r * s_new)**2: # Avoid machine precision
                    continue
            else:
                if n * (2 * s * s_new)**2 >= (r_new * s + r * s_new)**2:
                    continue
        if s_new <= d:
            return s_new, r_new
        
    return s,r

ans = 0

for n in range(2,100_001):
    if int(n**0.5)**2 != n:
        s,r = BestApproximation(n, 10**12)
        ans += s

print(ans)
