ans = 0
n = 50

# First suppose x1 = 0
for y1 in range(1, n+1): #x1 and y1 cannot both be 0        
    for x2 in range(1, n+1): # x1 and x2 cannot both be 0
        for y2 in range(0, y1+1): # One point cannot have both coordinates larger than the other
            a = y1**2
            b = x2**2 + y2**2
            c = x2**2 + (y2 - y1)**2
            if 2 * max(a,b,c) == a + b + c: # Pythagorean triplet
                ans += 1

for x1 in range(1, n+1):
    for y1 in range(0, n+1):
        # Firt suppose x1 == x2
        for y2 in range(0, y1): # y1 cannot be y2
            a = x1**2 + y1**2
            b = x1**2 + y2**2
            c = (y2 - y1)**2
            if 2 * max(a,b,c) == a + b + c: # Pythagorean triplet
                ans += 1
            
        for x2 in range(x1+1, n+1):  
            for y2 in range(0, y1+1):
                a = x1**2 + y1**2
                b = x2**2 + y2**2
                c = (x2 - x1)**2 + (y2 - y1)**2
                if 2 * max(a,b,c) == a + b + c: # Pythagorean triplet
                    ans += 1