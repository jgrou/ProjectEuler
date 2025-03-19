N = 32
M = 10  

Layers = [{} for _ in range(N+1)]
Layers[2][()] = set
Layers[3][()] = set

for n in range(4, N+1):
    for tuple1 in Layers[n-2]:
        new_tuple = tuple1 + (n-2,)
        neighbors = set()
        
        for tuple2 in Layers[n-3]:
            intersection = set(tuple1) & set(tuple2)
            if not intersection:
                neighbors.add(tuple2 + (n-3,))
            
        Layers[n][new_tuple] = neighbors
        
    for tuple1 in Layers[n-3]:
        new_tuple = tuple1 + (n-3,)
        neighbors = set()
        
        for tuple2 in Layers[n-2]:
            intersection = set(tuple1) & set(tuple2)
            if not intersection:
                neighbors.add(tuple2 + (n-2,))
            
        Layers[n][new_tuple] = neighbors
        
Layer = Layers[N]

W = [{} for _ in range(M+1)]

for n in range(2, M+1):
    for layer in Layer.keys():
        W[n][layer] = 0

for layer in Layer.keys():
    W[1][layer] = 1
    
for n in range(2, M+1):
    for layer in Layer.keys():
        for new_layer in Layer[layer]:
            W[n][new_layer] += W[n-1][layer]
            
ans = sum(W[M].values())