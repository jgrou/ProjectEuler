import math

# When a laser hits a mirror, instead of thinking of the laser reflecting, 
# you can think of the laser entering a new triangle that is a mirror image 
# of the first one. Repeatedly extending the picture this way results in an
# infinite grid of triangles. This solution works by iterating over the mirrored
# vertices of the row that corresponds to 12017639147 bounces, and counting 
# the vertices that are reachable, and correspond to vertex C.

surf = 12017639147
row = (surf + 3)//2

def IsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for k in range(3, int(n**0.5)+1, 2):
        if n%k == 0:
            return False
    return True

# The leftmost of each rowvertex is C,A,B,C,A,B,C,...
# The next vertices follow the same pattern: A,B,C,A,B,C,...
min_col = 3 - (row %3)
max_col = (row+1) // 2 - 1

if IsPrime(row):
    ans = 1 + (max_col - min_col) // 3
else:
    ans = 0
    for col in range(min_col, max_col + 1, 3):
       if math.gcd(row,col) == 1: # Otherwise we would have hit another vertex earlier
          ans += 1

print(2*ans)
