from fractions import Fraction 

n = 18

capacitance = Fraction(1, 1)
circuits = [set() for _ in range(n+1)]
circuits[1] = {capacitance} # Basic circuit using only 1 capacitor

for k in range(2,n+1):
    for size1 in range(1, k+1): # Split circuit of size k into two subcircuits of size1 and size2
        size2 = k - size1
        for circuit1 in circuits[size1]:
            for circuit2 in circuits[size2]:
                serial = circuit1 + circuit2
                circuits[k].add(serial)
                parallel = 1 / (1 / circuit1 + 1 / circuit2)
                circuits[k].add(parallel)
    
total = set()

for k in range(1, n+1):
    total |= circuits[k]