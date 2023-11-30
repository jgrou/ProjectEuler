import numpy as np

def Prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def has_complete_subgraph(matrix):
    n = matrix.shape[0]
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            if matrix[i, j] == 1:
                for k in range(j + 1, n - 1):
                    if matrix[i, k] == 1 and matrix[j, k] == 1:
                        for l in range(k + 1, n):
                            if matrix[i, l] == 1 and matrix[j, l] == 1 and matrix[k, l] == 1:
                                if matrix[i, n-1] == 1 and matrix[j, n-1] == 1 and matrix[k, n-1] == 1 and matrix[l, n-1] == 1:
                                    return [primes[i], primes[j], primes[k] ,primes[l], primes[n-1]]
    return None

primes = []
x = 3 # We can skip 2, as this always makes a concatenation even
index1 = 0
matrix = np.zeros((0, 0), dtype=int)
ans = 10**9
    
while x < ans:
    if Prime(x):
        new_matrix = np.zeros((index1+1,index1+1), dtype=int)
        new_matrix[:index1,:index1] = matrix
        matrix = new_matrix
        
        for index2, p in enumerate(primes):
            if Prime(int(str(p)+str(x))) and Prime(int(str(x)+str(p))):
                matrix[index2,index1] = 1
         
        primes.append(x)
        
        nodes = has_complete_subgraph(matrix)
        if nodes is not None:
            print(nodes)   
            if sum(nodes) < ans:
                ans = sum(nodes)
            
        index1 += 1
    x += 1