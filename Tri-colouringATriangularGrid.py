limit = 8
colours = ['r', 'g', 'b']
top_rows = {tuple(): 1}

def bottom_row(triangle, rows):
    res = {}

    for node_colors in triangle:
        configuration = tuple()
        seen = {}
        pos = 0
        for node in node_colors:
            if node[0] == rows-1:
                color = node_colors[node]
                if color not in seen:
                    seen[color] = pos # Position at which we first encounterd this color
                    pos += 1
                configuration += (colours[seen[color]],) # Which color doesn't matter
        if configuration in res:
            res[configuration] += 1
        else:
            res[configuration] = 1
    return res

def coloring(node_colors, check):
    if check == []:
        Triangle.append(node_colors)
        return
    
    new_node = check[0]
    row = new_node[0]
    col = new_node[1]
    neighbour_colors = set()
    
    if row & 1: # Upside down triangle: only to direct upper neighbor
        neighbour_colors.add(node_colors[(row-1, col)])
    elif row > 0: 
        if col > 0:
            neighbour_colors.add(node_colors[(row-1, col-1)])
        if col < row//2:
            neighbour_colors.add(node_colors[(row-1, col)])

    for color in colours:
        if color in neighbour_colors:
            continue
        new_node_colors = node_colors.copy()
        new_node_colors[new_node] = color
        coloring(new_node_colors, check[1:])

for height in range(1, limit+1):
    new_top_rows = {}
    
    # Create nodes
    nodes = (2 * height - 1) * [None]

    for col in range(height-1):
        nodes[col] = (2*height-3,col)

    for col in range(height):
        nodes[col+height-1] = (2*height-2,col)
    
    for top_row, count in top_rows.items():
        NodeColors = {}
        for i, color in enumerate(top_row):
            NodeColors[(2*height-4,i)] = color

        Triangle = []
        coloring(NodeColors, nodes)
        bottom_rows = bottom_row(Triangle, rows = 2 * height - 1)
        
        for tup, n in bottom_rows.items():
            if tup in new_top_rows:
                new_top_rows[tup] += count * n
            else:
                new_top_rows[tup] = count * n
    
    top_rows = new_top_rows

ans = sum(top_rows.values())