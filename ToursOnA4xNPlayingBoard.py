# https://oeis.org/A181688
limit = 8
ans = 0

#%% Finding all paths by recursion
grid = set()

for x in range(limit):
    for y in range(4):
        grid.add((x,y))
        
def Tours(location = (0,0), squares_left = grid):
    global ans
    x, y = location
    
    if x == 0 and y == 3: # We are in the bottom left corner
        if not squares_left: # We have visited everything
            ans += 1
        return
        
    if (x-1, y) in squares_left: # Move left
        new_squares_left = squares_left.copy()
        new_squares_left.remove((x-1,y))
        Tours((x-1,y), new_squares_left)
        
    if (x+1, y) in squares_left: # Move right
        new_squares_left = squares_left.copy()
        new_squares_left.remove((x+1,y))
        Tours((x+1,y), new_squares_left)
        
    if (x, y-1) in squares_left: # Move down
        new_squares_left = squares_left.copy()
        new_squares_left.remove((x,y-1))
        Tours((x,y-1), new_squares_left)
        
    if (x, y+1) in squares_left: # Move up
        new_squares_left = squares_left.copy()
        new_squares_left.remove((x,y+1))
        Tours((x,y+1), new_squares_left)
        
    return

grid.remove((0,0))
Tours()

#%%
a_1 = 8
a_2 = 4
a_3 = 1
a_4 = 1

for _ in range(4, limit):
    a_1, a_2, a_3, a_4 = (2*a_1 + 2 * a_2 - 2 *a_3 + a_4) % 10**8, a_1, a_2, a_3
    
#%%
import numpy as np

eigenvalues, eigenvectors = np.linalg.eig(np.array([[2, 2, -2, 1], [1, 0,0,0],[0,1,0,0],[0,0,1,0]]))
