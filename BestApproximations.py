import math

def continued_fraction_sqrt(n):
    """Compute the continued fraction representation of sqrt(n).
    
    Returns:
        (a0, [a1, a2, ..., a_{period}]) such that:
        sqrt(n) = a0 + 1 / (a1 + 1 / (a2 + ...))
    """
    m = 0
    d = 1
    a0 = a = int(math.isqrt(n))
    
    if a * a == n:
        return (a, [])  # n is a perfect square

    period = []
    seen = {}

    while (m, d, a) not in seen:
        seen[(m, d, a)] = True
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)

    return (a0, period)

def BestApproximation(n, d):
    a0, period = continued_fraction_sqrt(n)

    r_new = a0
    r = 1
    s_new = 1
    s = 0
    i = 0
    n = len(period)

    while s_new <= d:
        r_new, r, r_old = period[i%n] * r_new + r, r_new, r
        s_new, s, s_old = period[i%n] * s_new + s, s_new, s
        i += 1

    # Truncate the continued fraction, and reduce its last term by a chosen amount (possibly zero)
    a_k = a = period[(i-1)%n]
    even = not (a_k&1)

    while s_new > d:
        a -= 1
        if a < (a_k + 1) // 2: # The reduced term cannot have less than half its original value.
            return s
        
        r_new = a * r + r_old
        s_new = a * s + s_old
        # If the final term is even, half its value is admissible only if the corresponding semiconvergent is
        # better than the previous convergent. 
        if a == (a_k) // 2 and even: 
            if abs(r / s - n**0.5) <= abs(r_new / s_new - n**0.5):
                return s
    return s_new

ans = 0

for n in range(2, 100_001):
    if round(n**0.5)**2 != n:
        ans += BestApproximation(n, 10**12)
