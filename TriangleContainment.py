def containment(triangle):
    # Count number of point above the x-axis
    upper = []
    for i in range(3):
        if triangle[2*i+1] > 0:
            upper.append(i)
    
    # If all poinst lie on the same side of the x-axis it is not possible
    if len(upper) == 0 or len(upper) ==3:
        return False
    
    lower = [i for i in range(3) if i not in upper]
    x_upper = [triangle[2*i] for i in upper]
    x_lower = [triangle[2*i] for i in lower]
    y_upper = [triangle[2*i+1] for i in upper]
    y_lower = [triangle[2*i+1] for i in lower]
    
    if len(upper) == 1:
        x1 = (y_upper[0] * x_lower[0] - y_lower[0] * x_upper[0]) / (y_upper[0] - y_lower[0])
        x2 = (y_upper[0] * x_lower[1] - y_lower[1] * x_upper[0]) / (y_upper[0] - y_lower[1])
        
    if len(upper) == 2:
        x1 = (y_upper[0] * x_lower[0] - y_lower[0] * x_upper[0]) / (y_upper[0] - y_lower[0])
        x2 = (y_upper[1] * x_lower[0] - y_lower[0] * x_upper[1]) / (y_upper[1] - y_lower[0])

    if x1 * x2 > 0: # If both lines cross the x-axis at the same side, 0 is not in the triangle
        return False
    else:
        return True
    
ans = 0

with open('triangles.txt') as f:
    for line in f:
        numbers = line.strip().split(',')
        triangle = [int(num) for num in numbers]
        if containment(triangle):
            ans += 1