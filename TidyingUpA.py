import math
import time

def find_paths(matrix, path, i, j, result, rows, cols):
    # If we reach the bottom-right corner, add the path to the result list
    if i == rows - 1 and j == cols - 1:
        # Add the final piece that makes everything one segment again
        result.append(path[:] + [1])
        return

    # Move Down
    if i + 1 < rows:
        path.append(matrix[i + 1][j])
        find_paths(matrix, path, i + 1, j, result, rows, cols)
        path.pop()  # Backtrack

    # Move Right
    if j + 1 < cols:
        path.append(matrix[i][j + 1])
        find_paths(matrix, path, i, j + 1, result, rows, cols)
        path.pop()  # Backtrack
        
def Product(tuple1, tuple2):
    cols = len(tuple1)
    rows = len(tuple2)
    matrix = [cols * [None] for _ in range(rows)]
    
    for i1, t1 in enumerate(tuple1):
        for i2, t2 in enumerate(tuple2):
            matrix[i2][i1] = t1 + t2
            
    result = []
    path = [matrix[0][0]]
    find_paths(matrix, path, 0, 0, result, rows, cols)
    return result

start = time.time()
limit = 15
ans = 0
list_of_dictionaries = (limit+1) * [None]
list_of_dictionaries[0] = {(0,):1}
list_of_dictionaries[1] = {(0,1):1}

for n in range(2,limit+1):
    dictionary = {}

    for last_piece in range(1, (n+1)//2 + 1):
        # If left or right is bigger, doesn't matter
        if last_piece == (n+1)/2:
            multiplier = 1
        else:
            multiplier = 2
        left_dict = list_of_dictionaries[last_piece-1]
        right_dict = list_of_dictionaries[n-last_piece]
        
        for left_key, left_item in left_dict.items():
            for right_key, right_item in right_dict.items():
                for t in Product(left_key, right_key):
                    if tuple(t) in dictionary:
                        dictionary[tuple(t)] += left_item * right_item * multiplier
                    else:
                        dictionary[tuple(t)] = left_item * right_item * multiplier
                
    list_of_dictionaries[n] = dictionary
    
for key, value in dictionary.items():
    ans += max(key) * value
    
ans /= math.factorial(limit)
print(ans)
print(time.time() - start)