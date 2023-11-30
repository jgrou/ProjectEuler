matrix = []

with open('matrix.txt') as f:
    for line in f:
        row = [int(num) for num in line.strip().split(',')]
        matrix.append(row)  # Splitting the line into words
        
n = len(matrix)

for i in range(1,n):
    matrix[0][i] += matrix[0][i-1]
    matrix[i][0] += matrix[i-1][0]
    
for i in range(1,n):
    for j in range(i,n):
        matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
    for j in range(i+1,n):
        matrix[j][i] += min(matrix[j-1][i], matrix[j][i-1])
        
ans = matrix[n-1][n-1]
