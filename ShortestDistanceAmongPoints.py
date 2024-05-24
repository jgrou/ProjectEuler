limit = 2_000_000

px = 290797
py = px**2 % 50515093
s = [(px,py)]

for _ in range(limit - 1):
    px_new = py**2 % 50515093
    py_new = px_new**2 % 50515093
    s.append((px_new, py_new))
    px, py = px_new, py_new
    
sorted_x = sorted(s, key=lambda x: x[0])

def ShortestDistance(points):
    if len(points) == 1:
        return 2 * 50515093
    
    median = len(points) // 2
    x_median = points[median][0]
    
    d1 = ShortestDistance(points[:median])
    d2 = ShortestDistance(points[median:])
    
    delta = min(d1, d2)
    
    # Now check for all points in a strip from [median-delta, median+delta]
    middle = [point for point in points if abs(point[0] - x_median) < delta]
    middle = sorted(middle, key=lambda x: x[1]) # In theory sorting before is better, in practice sorting here is faster
    
    min_d = 2 * 50515093
    n = len(middle)
    
    for i in range(n):
        p1 = middle[i]
        for j in range(i+1, min(i+12,n)):
            p2 = middle[j]
            d = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5 
            if d < min_d:
                min_d = d
    
    return min(delta, min_d)

ans = ShortestDistance(sorted_x)