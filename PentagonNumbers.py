MinDiff = 10**9
PentagonNumbers = [1]
n = 2
Pn = 5

while 2 * PentagonNumbers[-1] - Pn <= MinDiff:
    for Pk in PentagonNumbers:
        if Pn - Pk in PentagonNumbers:
            diff = 2 * Pk - Pn
            if diff in PentagonNumbers:
                if diff < MinDiff:
                    MinDiff = diff
                    pair = [Pn - Pk, Pk]
    PentagonNumbers.append(Pn)
    n += 1
    Pn = int(0.5* n * (3 * n - 1))