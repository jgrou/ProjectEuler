import numpy as np

def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

u_n = []
ans = 0

for k in range(1,11):
    u_n.append(u(k))
    
    matrix = np.zeros((k,k))
    
    for n_row in range(k):
        for n_column in range(k):
            matrix[n_row,n_column] = (n_row+1)**(k-1-n_column)
            
    BOP = np.linalg.solve(matrix, u_n)
    FIT = 0
    
    for i in range(k):
        FIT += BOP[i] * (k+1)**(k-1-i)
    
    ans += FIT