import math

n = 286

while True:
    Tn = n * (n+1) / 2 # Compute next triangular number
    if ((math.sqrt(1 + 24 * Tn) + 1) / 6) % 1 == 0: # Check if pentagonal
        if ((math.sqrt(1 + 8 * Tn) + 1) / 4) % 1 == 0: # Check if hexagonal
            ans = Tn
            break
    n += 1
            