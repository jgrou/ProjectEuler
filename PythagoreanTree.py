import numpy as np

alpha = np.arcsin(4/5) # Angle opposite 4/5
beta = np.arcsin(3/5) # Angle opposite 3/5

min_x = 0.0
min_y = 0.0
max_x = 1.0
max_y = 1.0

def NewLayer(corner1, corner2, length, angle, t=1, direction='min_x'):
    if length < 1e-13: # This is empirically the needed limit
        return
    
    global min_x, max_x, max_y, min_y
    
    min_x = min(corner1[0], corner2[0], min_x)
    max_x = max(corner1[0], corner2[0], max_x)
    max_y = max(corner1[1], corner2[1], max_y)
    min_y = min(corner1[1], corner2[1], min_y)
    
    new_length1 = 4/5 * length
    new_angle1 = angle + beta
    triangle_point = (corner1[0] + new_length1 * np.cos(new_angle1), corner1[1] + new_length1 * np.sin(new_angle1))
    left1 = (corner1[0] + new_length1 * np.cos(np.pi/2 + new_angle1), corner1[1] + new_length1 * np.sin(np.pi/2 + new_angle1))
    left2 = (left1[0] + triangle_point[0] - corner1[0], left1[1] + triangle_point[1] - corner1[1])
    
    new_length2 = 3/5 * length
    new_angle2 = angle - alpha
    right1 = (corner2[0] + new_length2 * np.cos(np.pi/2 + new_angle2), corner2[1] + new_length2 * np.sin(np.pi/2 + new_angle2))
    right2 = (right1[0] + triangle_point[0] - corner2[0], right1[1] + triangle_point[1] - corner2[1])

    if direction == 'min_x':
        left = min(left1[0], left2[0]) < min(right1[0], right2[0])
    elif direction == 'max_x':
        left = max(left1[0], left2[0]) > max(right1[0], right2[0])
    elif direction == 'max_y':
        left = max(left1[1], left2[1]) > max(right1[1], right2[1])
    elif direction == 'min_y':
        left = min(left1[1], left2[1]) < min(right1[1], right2[1]) or t==1

    if left:
        NewLayer(left1, left2, new_length1, new_angle1, t+1, direction)
    else:
        NewLayer(right2, right1, new_length2, new_angle2, t+1, direction)
    
NewLayer((0,1), (1,1), 1, 0, 1, 'min_x')
NewLayer((0,1), (1,1), 1, 0, 1, 'max_x')
NewLayer((0,1), (1,1), 1, 0, 1, 'max_y')
NewLayer((0,1), (1,1), 1, 0, 1, 'min_y')
ans = (max_x - min_x) * (max_y - min_y)
print(round(ans,10))