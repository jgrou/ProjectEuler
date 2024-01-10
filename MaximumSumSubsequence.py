import numpy as np

# Generate numbers
N = 2000
s = N**2 * [None]

for k in range(55):
    s[k] = (100003 - 200003 * (k+1) + 300007 * (k+1)**3)% 1000000 - 500000
    
for k in range(55, N**2):
    s[k] = (s[k-24] + s[k-55] + 1000000)%1000000 - 500000

table = np.array(s).reshape(2000,2000)

# Horizontal
horizontal_table = table.copy()

for i in range(N):
    for j in range(1,N):
        if horizontal_table[i,j-1] > 0:
            horizontal_table[i,j] += horizontal_table[i,j-1]

horizontal_max = np.max(horizontal_table)

# Vertical
vertical_table = table.copy()

for i in range(N):
    for j in range(1,N):
        if vertical_table[j-1,i] > 0:
            vertical_table[j,i] += vertical_table[j-1,i]
     
vertical_max = np.max(vertical_table)

# Diagonal
diagonal_table = table.copy()

# Diagonals starting at uppper row
for i in range(N):
    for j in range(1,N-i):
        if diagonal_table[j-1,i+j-1] > 0:
            diagonal_table[j,i+j] += diagonal_table[j-1,i+j-1]

# Diagnoals starting at first column
for i in range(1,N): # except first row
    for j in range(1,N-i):
        if diagonal_table[i+j-1,j-1] > 0:
            diagonal_table[i+j,j] += diagonal_table[i+j-1,j-1]

diagonal_max = np.max(table)

#Anti-diagonal
anti_diagonal_table = table.copy()

# Anti-diagonals starting at first column
for i in range(N):
    for j in range(1,i+1):
        if anti_diagonal_table[i-j+1,j-1] > 0:
            anti_diagonal_table[i-j,j] += anti_diagonal_table[i-j+1,j-1]

# Anti-diagonals starting at bottown row
for i in range(1,N): # Except first column
    for j in range(1,N-i):
        if anti_diagonal_table[N-j,i+j-1] > 0:
            anti_diagonal_table[N-1-j,i+j] += anti_diagonal_table[N-j,i+j-1]
     
anti_diagonal_max = np.max(anti_diagonal_table)

answer = max(horizontal_max, vertical_max, diagonal_max, anti_diagonal_max)