lim = 1000

for c in range(1, lim): # Angle of at most 120 degrees
    for b in range(int(c/3**0.5), c+1):
        mina = 2/3**0.5 * c - b
        for a in range(int(mina), b+1):
            x_C = (c**2 + b**2 - a**2) / (2 * c) # x coordinate of C, A is at (0,0) and B at (c,0)
            y_C = (b**2 - x_C**2)**0.5 # y coordinate of C
            
            # Find the point O which is in the middle down AB
            x_O = c / 2
            y_O = 3**0.5 * x_O
            
            # Find N by solving quadritc equation
            a_N = 4 * (c - x_C)**2 +2 * y_C**2
            b_N = 2 * (x_C * c**2 - c * y_C**2 - x_C * y_C **2 - c**3)
            c_N = y_C**4 + c**4 - 2 * y_C**2 * a
            
            x_N = -b + (b**2 - 4 * a * c)**0.5 / (2 * a)
            y_N = (a - (x_N - x_C)**2)**0.5
            
            # Find intersection of AN and OC
            