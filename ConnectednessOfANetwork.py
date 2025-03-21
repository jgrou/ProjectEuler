# Find function with path compression
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Union function with size-based merging
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if size[rootX] > size[rootY]:
            parent[rootY] = rootX
            size[rootX] += size[rootY]
        else:
            parent[rootX] = rootY
            size[rootY] += size[rootX]

S = [0]
size = 10**6 * [1]
parent = [i for i in range(10**6)]
ans = 0

for k in range(1, 56):
    S.append((100003 - 200003 * k + 300007 * k**3) % 1000000)
    
    if (not(k&1)) and (S[k-1] != S[k]):
        union(S[k-1], S[k])
        ans += 1
        
while size[find(524287)] < 990_000:
    k += 1
    S_new = (S[-24] + S[-55]) % 10**6
    S = S[1:] + [S_new]
    
    if (not(k&1)) and (S[-1] != S[-2]):
        union(S[-1], S[-2])
        ans += 1
        