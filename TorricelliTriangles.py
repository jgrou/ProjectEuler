lim = 1000
values = set()

for c in range(1, lim): # Angle of at most 120 degrees
    for b in range(int(c/3**0.5), c+1):
        mina = max(1, 2/3**0.5 * c - b)
        for a in range(int(mina), b+1):
            x_C = (c**2 + b**2 - a**2) / (2 * c) # x coordinate of C, A is at (0,0) and B at (c,0)
            y_C = (b**2 - x_C**2)**0.5 # y coordinate of C
            
            # Find the point O which is in the middle down AB
            x_O = c / 2
            y_O = -3**0.5 * x_O
            
            # Find N by solving quadritc equation
            a_N = 4 * (c - x_C)**2 + 4 * y_C**2
            b_N = 4 * (c - x_C) * (y_C**2 + x_C**2 - c**2) - 8 * c * y_C**2
            c_N = (y_C**2 + x_C**2 - c**2)**2 - 4 * y_C**2 * a**2 + 4 * y_C**2 * c**2
            
            x_N = (-b_N + (b_N**2 - 4 * a_N * c_N)**0.5) / (2 * a_N)
            y_N = (a**2 - (x_N - c)**2)**0.5
            
            # Find intersection of AN and OC
            rc_AN = y_N / x_N
            if x_C == x_O:
                x_T = x_C
            else:
                rc_OC = (y_C - y_O) / (x_C - x_O)
                x_T = (y_O - rc_OC * x_O) /  (rc_AN - rc_OC)
            y_T = rc_AN * x_T
            
            # Calculate distance to T
            p = (x_T**2 + y_T**2)**0.5 # Distance AT
            q = ((x_C - x_T)**2 + (y_C - y_T)**2)**0.5 # Distance CT
            r = ((c - x_T)**2 + y_T**2)**0.5 # Distance BT
            
            if int(round(p,10)) == round(p,10) and int(round(p,10)) == round(p,10) and int(round(p,10)) == round(p,10):
                print(p+q+r)
                values.add(p+q+r)