# Initial condtions
hits = 0
x = 0.0
y = 10.1
rc = -19.7/1.4

while True:
    # Solve a quadratic equation to find the location where the laser beam hits the ellipse
    a = 4 + rc**2
    b = 2 * y * rc - 2 * x * rc**2
    c = y**2 - 2 * y * rc * x + x**2 * rc**2 - 100
    
    x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
    x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
    
    # One of the cutting points between the laser beam and the ellipse is the previous point itself
    if abs(x-x1) > abs(x-x2): 
        x_new = x1
    else:
        x_new = x2
        
    y = y + (x_new - x) * rc
    x = x_new
    
    # From some complicated tangent formula's, this is the new rc
    m = -4 * x / y
    rc = (2 * m - rc * (1 - m**2)) / (1 - m**2 + 2 * m * rc)
    
    if abs(x) <= 0.01 and y > 0: # we are out
        break
    
    hits += 1