import math

L_max = 10**8
m_max = int(0.5 * ((1 + 2 * L_max)**0.5 - 1)) # a = m^2 - n^2, b = 2 mn, c = m^2 + n^2, m>n
ans = 0

for m in range(1, m_max + 1):
    n_max = min(int(L_max / (2 * m) - m), m - 1)
    if m%2 == 1: # m,n not both odd
        for n in range(2, n_max + 1, 2):
            if math.gcd(m, n) == 1:
                c = m**2 + n**2 
                diff = 2 * m *n + n**2 - m**2 
                if c % diff == 0: # Tiling exists if c is multiple of b-a
                    L = (2 * m * (m + n))
                    temp = L
                    while temp < L_max:
                        ans += 1
                        temp += L
    else:
        for n in range(1, n_max + 1):
            if math.gcd(m, n) == 1:
                c = m**2 + n**2
                diff = 2 * m *n + n**2 - m**2
                if c % diff == 0:
                    L = (2 * m * (m + n))
                    temp = L
                    while temp < L_max:
                        ans += 1
                        temp += L