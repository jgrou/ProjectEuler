import itertools

squares = [(0,1), (0,4), (0,9), (1,6), (2,5), (3,6), (4,9), (6,4), (8,1)]
ans = 0

def Check(Cube1, Cube2):
    # Make the extended set for both cubes
    if 6 in Cube1:
        Cube1 = Cube1 + (9,)
    if 9 in Cube1:
        Cube1 = Cube1 + (6,)
    if 6 in Cube2:
        Cube2 = Cube2 + (9,)
    if 9 in Cube2:
        Cube2 = Cube2 + (6,)
    
    # Check if all number can be formed
    for (i,j) in squares:
        if i not in Cube1 or j not in Cube2:
            if i not in Cube2 or j not in Cube1:
                return False
    return True

permutations = list(itertools.combinations(range(10),6))

for k in range(len(permutations)):
    for l in range(k+1, len(permutations)):
        if Check(permutations[k], permutations[l]):
            ans += 1