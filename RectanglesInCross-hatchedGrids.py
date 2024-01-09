def NumberOfRectangles(n,m):
    if n > m: # Symmetric problem, assume m >= n
        return NumberOfRectangles(m, n)
    
    straight = n * m * (n + 1) * (m + 1) / 4 # Number of rectangles formed by the straight lines
    skew = 0
    
    def StartStop(z): # Find start and end x-coordinates given y-coordinate or vice versa
        if z < n:
            start = n - z
        else:
            start = z + 1 - n
        if z < m:
            end = n + z - 1
        else:
            end = 2 * m + n - 2 - z            
        return start, end
        
    for y in range(1, m+n-1):
        x_start, x_end = StartStop(y)
        for x in range(int(x_start), int(x_end) + 1):
            y_start, y_end = StartStop(x)
            skew += (y_end + 1 - max(y, y_start)) * (x_end + 1 - x)

    return straight + skew

M = 3
N = 3
ans = 0

for n in range(1,N+1):
    for m in range(1,M+1):
        ans += NumberOfRectangles(n,m)