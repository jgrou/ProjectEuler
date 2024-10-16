import math
import time

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
        
start = time.time()
limit = 15
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
print(time.time() - start)
