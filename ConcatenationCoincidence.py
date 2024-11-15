theta = '2.'
i = 2

while len(theta) < 26:
    b = (i+1) * [None]
    a = (i+1) * [None]
    b[1] = float(theta)
    a[1] = int(b[1])
    
    for n in range(2,i+1):
        b[n] = int(b[n-1]) * (b[n-1] - int(b[n-1]) + 1)
        a[n] = int(b[n])
    theta += str(a[i])
    i += 1
    
print(theta)