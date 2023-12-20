import numpy as np

x_boundary = 0.01
hits = 0
x = 0.0
y = 10.1
rc = -19.7/1.4

while True:
    a = 4 + rc**2
    b = 2 * y * rc - 2 * x * rc**2
    c = y**2 - 2 * y * rc * x + x**2 * rc**2 - 100
    
    x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
    x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
    
    if abs(x-x1) > abs(x-x2): # One of the cutting points is the previous point itself
        x_new = x1
    else:
        x_new = x2
        
    y = y + (x_new - x) * rc
    x = x_new
    
    m = -4 * x / y
    
    alpha = np.arctan(m) # Angle of the tangent
    beta = np.arctan(-rc) + alpha - np.pi / 2 # Angle of incidence
    rc = -np.tan(np.pi/2 - alpha - beta)
    
    
    if abs(x) <= x_boundary and y>0:
        break
    
    hits += 1