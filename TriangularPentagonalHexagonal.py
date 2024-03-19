n = 286

while True:
    Tn = n * (n+1) / 2 # Compute next triangular number
    if (((1 + 24 * Tn)**0.5 + 1) / 6) % 1 == 0: # Check if pentagonal
        if (((1 + 8 * Tn)**0.5 + 1) / 4) % 1 == 0: # Check if hexagonal
            ans = Tn
            break
    n += 1
