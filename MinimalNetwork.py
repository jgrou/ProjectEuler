network = []

with open('network.txt') as f:
    for lines in f:
        line = lines.strip().split(',')
        row = []
        for i in line:
            if i == '-':
                row.append(i)
            else:
                row.append(int(i))
        network.append(row)
        
E = []
total_weight = 0

# Create list of edges
for i in range(len(network)):
    for j in range(i+1, len(network)):
        if network[i][j] != '-':
            E.append([i,j,network[i][j]])
            total_weight += network[i][j]

E = sorted(E, key=lambda x: x[2]) # Order edges by weights
F = [[i] for i in range(len(network))] # Create forest where each vertex in the graph is a seperate tree
i = 0
weight = 0

while len(F) != 1:
    v = E[i]
    for tree in F:
        if v[0] in tree:
            tree1 = tree
        if v[1] in tree:
            tree2 = tree
    if tree1 != tree2:
        new_tree = list(set(tree1) | set(tree2)) # If the edge connects different trees add it and merge the trees
        F.remove(tree1)
        F.remove(tree2)
        F.append(new_tree)
        weight += v[2]
    i += 1
    
ans = total_weight - weight