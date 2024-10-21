limit = 15

#%% My solution
import math

def find_paths(tuple1, tuple2, path, i, j, result, rows, cols):
    # Add the final piece that makes everything one segment again
    if i == rows - 1 and j == cols - 1:
        result.append(path + [1])
        return

    # Place left piece
    if i + 1 < rows:
        path.append(tuple1[i + 1] + tuple2[j])
        find_paths(tuple1, tuple2, path, i + 1, j, result, rows, cols)
        path.pop()

    # Place right piece
    if j + 1 < cols:
        path.append(tuple1[i] + tuple2[j + 1])
        find_paths(tuple1, tuple2, path, i, j + 1, result, rows, cols)
        path.pop()

ans = 0
list_of_dictionaries = (limit+1) * [None]
list_of_dictionaries[0] = {(0,): 1}

for n in range(1, limit+1):
    dictionary = {}

    for last_piece in range(1, (n+1)//2 + 1):
        multiplier = 1 if last_piece == (n+1)/2 else 2 # If left or right is bigger, doesn't matter
        left_dict = list_of_dictionaries[last_piece-1]
        right_dict = list_of_dictionaries[n-last_piece]
        
        for left_key, left_item in left_dict.items():
            for right_key, right_item in right_dict.items():
                # For two tuples compute every combination of placing left and right: math.comb(cols+rows, cols)
                rows = len(right_key)
                cols = len(left_key)
                result = [] # Using yield goes slower
                path = [0]
                find_paths(right_key, left_key, path, 0, 0, result, rows, cols)
                
                for t in result:
                    t_tuple = tuple(t)
                    if t_tuple in dictionary:
                        dictionary[t_tuple] += left_item * right_item * multiplier
                    else:
                        dictionary[t_tuple] = left_item * right_item * multiplier

    list_of_dictionaries[n] = dictionary

for key, value in dictionary.items():
    ans += max(key) * value

ans /= math.factorial(limit)
print(round(ans,6))

#%%
import numpy as np

N = limit + 3

# Create a 5-dimensional array initialized to zeros
f = np.zeros((N, N, N, 2, 2))

# Initialize base cases
f[1][1][1][0][1] = f[1][1][1][0][0] = f[1][1][1][1][0] = 1

# Main nested loops
for i in range(1, limit):
    for j in range(1, limit+1):
        for k in range(limit+1):
            for p in range(2):
                for q in range(2):
                    if f[i][j][k][p][q] == 0:
                        continue
                    if k == 1 and p == 1 and q == 1:
                        continue
                    
                    nk = k - 1
                    if p == 0:
                        if k > 0:
                            f[i+1][j][k][1][q] += f[i][j][k][p][q]
                            f[i+1][j][k][0][q] += f[i][j][k][p][q]
                        f[i+1][max(j, k+1)][k+1][1][q] += f[i][j][k][p][q]
                        f[i+1][max(j, k+1)][k+1][0][q] += f[i][j][k][p][q]
                    
                    if q == 0:
                        if k > 0:
                            f[i+1][j][k][p][1] += f[i][j][k][p][q]
                            f[i+1][j][k][p][0] += f[i][j][k][p][q]
                        f[i+1][max(j, k+1)][k+1][p][1] += f[i][j][k][p][q]
                        f[i+1][max(j, k+1)][k+1][p][0] += f[i][j][k][p][q]
                    
                    if i == 0:
                        nk = 1
                    
                    if k > 1:
                        f[i+1][j][k-1][p][q] += nk * f[i][j][k][p][q]
                    if k > 0:
                        f[i+1][j][k][p][q] += nk * 2 * f[i][j][k][p][q]
                    f[i+1][max(j, k+1)][k+1][p][q] += nk * f[i][j][k][p][q]

# Calculate the final answer
num = 0
den = 0

for j in range(1, limit+1):
    v = f[limit][j][1][1][1]
    if v == 0:
        break
    num += j * v
    den += v

# Print the final result
print(f"{num / den:.6f}")

#%% ProjectEuler Solution
# Memoization cache
memo = [[[{} for _ in range((limit+1)//2 + 1)] for _ in range(limit)] for _ in range(limit)]

# Solve function
def solve(L, R, M, maxSoFar, leftSpaces):
    if R < L:
        L, R = R, L
    M.sort()
    assert len(M) == 0 or M[0] > 0
    maxSoFar = max(maxSoFar, len(M) + 1)
    
    if tuple(M) in memo[L][R][maxSoFar]:
        return memo[L][R][maxSoFar][tuple(M)]
    
    res = 0.0
    if leftSpaces == 0:
        memo[L][R][maxSoFar][tuple(M)] = maxSoFar
        return maxSoFar
    
    for i in range(L-1):
        M2 = M[:]
        M2.append(L-1-i)
        res += solve(i, R, M2, maxSoFar, leftSpaces-1)
    
    if L > 0:
        res += solve(L-1, R, M, maxSoFar, leftSpaces-1)
    
    for i in range(R-1):
        M2 = M[:]
        M2.append(R-1-i)
        res += solve(L, i, M2, maxSoFar, leftSpaces-1)
    
    if R > 0:
        res += solve(L, R-1, M, maxSoFar, leftSpaces-1)
    
    for i in range(len(M)):
        for j in range(M[i]):
            M2 = M[:]
            del M2[i]
            if j > 0:
                M2.append(j)
            if M[i] - 1 - j > 0:
                M2.append(M[i] - 1 - j)
            res += solve(L, R, M2, maxSoFar, leftSpaces-1)
    
    memo[L][R][maxSoFar][tuple(M)] = res
    return res

# Main code execution
sum_result = 0.0
for i in range(limit):
    sum_result += solve(i, limit-1-i, [], 1, limit-1)
    
for i in range(2, limit+1):
    sum_result /= i
    
print(f"{sum_result:.6f}")