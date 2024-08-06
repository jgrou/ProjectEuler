import numpy as np

def P(m):
    matrix = np.zeros((m-1,m-1))
    vector = np.zeros(m-1)
    
    for k in range(2, m+1):
        row = k * np.ones(m-1)
        row[k-2] += 1
        
        matrix[k-2] = row
        vector[k-2] = k * m
        
    x = np.linalg.solve(matrix, vector)
    res = m - sum(x)
    
    for k in range(2, m+1):
        res *= x[k-2]**k
        
    return res

ans = 0

for m in range(2,16):
    ans += int(P(m))