import math

L_max = 1_500_001
m_max = int(0.5 * ((1 + 2 * L_max)**0.5 - 1))
lst = []

for m in range(1, m_max + 1):
    n_max = min(int(L_max / (2 * m) - m), m - 1)
    if m%2 == 1: # m,n not both odd
        for n in range(2, n_max + 1, 2):
            if math.gcd(m, n) == 1:
                L = (2 * m * (m + n))
                temp = L
                while temp < L_max:
                    lst.append(temp)
                    temp += L
    else:
        for n in range(1, n_max + 1):
            if math.gcd(m, n) == 1:
                L = (2 * m * (m + n))
                temp = L
                while temp < L_max:
                    lst.append(temp)
                    temp += L

element_count = {}
    
# Count occurrences of each element in the list
for element in lst:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1
    
# Count elements that occur only once
ans = 0
for element, occurrence in element_count.items():
    if occurrence == 1:
        ans += 1