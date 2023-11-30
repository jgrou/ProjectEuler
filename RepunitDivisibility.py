n = 10**6 # n > An
An = 0

while An <= 10**6:
    n += 1
    if n%2 == 0 or n%5==0:
        continue
    An = 1
    R = 1
    while R%n > 0:
        R = (10 * R + 1) % n
        An += 1