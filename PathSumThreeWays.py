matrix = []

with open('matrix.txt') as f:
    for line in f:
        row = [int(num) for num in line.strip().split(',')]
        matrix.append(row)  # Splitting the line into words

n = len(matrix)

def dijkstra(graph):
    # Initialize distances with infinity and the start nodes with weight
    distance = [[float('inf') for i in range(n)] for j in range(n)]
    for j in range(n):
        distance[j][0] = graph[j][0]
    unvisited = [(i,j) for i in range(n) for j in range(n)]
    
    while len(unvisited) != 0:
        # Find smallest element index in unvisted set
        min_value = float('inf')

        for k in unvisited:
            value = distance[k[0]][k[1]]
            if value < min_value:
                min_value = value
                curr_i, curr_j = k
                
        if curr_i < n-1:
            distance[curr_i+1][curr_j] = min(distance[curr_i+1][curr_j], distance[curr_i][curr_j] + graph[curr_i+1][curr_j])
        if curr_i > 0:
            distance[curr_i-1][curr_j] = min(distance[curr_i-1][curr_j], distance[curr_i][curr_j] + graph[curr_i-1][curr_j])
        if curr_j < n-1:
            distance[curr_i][curr_j+1] = min(distance[curr_i][curr_j+1], distance[curr_i][curr_j] + graph[curr_i][curr_j+1])
        unvisited.remove((curr_i, curr_j))

    return distance

distances = dijkstra(matrix)
minimum = min([distances[i][n-1] for i in range(n)])