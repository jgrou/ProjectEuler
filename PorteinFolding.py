import itertools

def NewConfiguration(configuration, visited, x_coor, y_coor, step, res, string):
    if step == len(string):
        yield res
        return
    
    original_x = x_coor
    original_y = y_coor
    original_res = res
    
    # Move to the right
    x_coor = original_x + 1
    if (x_coor, original_y) not in visited:
        visited.add((x_coor, original_y))
        if string[step] == 'H':
            res += ((x_coor-1, original_y) in configuration) + \
                   ((x_coor+1, original_y) in configuration) + \
                   ((x_coor, original_y-1) in configuration) + \
                   ((x_coor, original_y+1) in configuration)
            configuration.add((x_coor, original_y))
        yield from NewConfiguration(set(configuration), visited, x_coor, original_y, step+1, res, string)
        if string[step] == 'H':
            configuration.remove((x_coor, original_y))
        visited.remove((x_coor, original_y))
        res = original_res
    
    # Move to the left
    x_coor = original_x - 1
    if (x_coor, original_y) not in visited:
        visited.add((x_coor, original_y))
        if string[step] == 'H':
            res += ((x_coor-1, original_y) in configuration) + \
                   ((x_coor+1, original_y) in configuration) + \
                   ((x_coor, original_y-1) in configuration) + \
                   ((x_coor, original_y+1) in configuration)
            configuration.add((x_coor, original_y))
        yield from NewConfiguration(set(configuration), visited, x_coor, original_y, step+1, res, string)
        if string[step] == 'H':
            configuration.remove((x_coor, original_y))
        visited.remove((x_coor, original_y))
        res = original_res
    
    # Move up
    y_coor = original_y + 1
    if (original_x, y_coor) not in visited:
        visited.add((original_x, y_coor))
        if string[step] == 'H':
            res += ((original_x-1, y_coor) in configuration) + \
                   ((original_x+1, y_coor) in configuration) + \
                   ((original_x, y_coor-1) in configuration) + \
                   ((original_x, y_coor+1) in configuration)
            configuration.add((original_x, y_coor))
        yield from NewConfiguration(set(configuration), visited, original_x, y_coor, step+1, res, string)
        if string[step] == 'H':
            configuration.remove((original_x, y_coor))
        visited.remove((original_x, y_coor))
        res = original_res
    
    # Move down
    y_coor = original_y - 1
    if (original_x, y_coor) not in visited:
        visited.add((original_x, y_coor))
        if string[step] == 'H':
            res += ((original_x-1, y_coor) in configuration) + \
                   ((original_x+1, y_coor) in configuration) + \
                   ((original_x, y_coor-1) in configuration) + \
                   ((original_x, y_coor+1) in configuration)
            configuration.add((original_x, y_coor))
        yield from NewConfiguration(set(configuration), visited, original_x, y_coor, step+1, res, string)
        if string[step] == 'H':
            configuration.remove((original_x, y_coor))
        visited.remove((original_x, y_coor))
        res = original_res

ans = 0

for string in itertools.product('HP',repeat=15):
    visited = {(0,0), (1,0)}
    positions_H = set()
    current = 0
    
    if string[0] == 'H':
        positions_H.add((0,0))
    if string[1] == 'H':
        positions_H.add((1,0))
    if len(positions_H) == 2:
        current = 1
        
    maximum = 0
    
    for n in NewConfiguration(positions_H, visited, 1, 0, 2, current, string):
        maximum = max(maximum,n)
        
    ans += maximum
    
print(ans)