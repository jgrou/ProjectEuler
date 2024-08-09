import itertools

# check each protein whether the current grid is better than anything seen before
def optimize(grid):
    contacts = [] # list of neighbors
    seen = 0 # count how many occupied cells I've seen

    # extremely straight foldings can't be optimal because they have only contacts between direct neighbors
    ignoreStraight = 9  # empirical value
    if length != 15:
        ignoreStraight = 0

    # walk through the grid
    for i in range(ignoreStraight, GridSize - 1 - ignoreStraight):
        for j in range(ignoreStraight, GridSize - 1 - ignoreStraight):
            # already visited the entire protein?
            if seen + 1 >= length:
                break

            # ignore None cells
            if grid[i][j] == None:
                continue

            # one more element visited
            seen += 1
            # get its index (0..length-1)
            from_idx = grid[i][j]

            # check right neighbor
            if grid[i + 1][j] != None:
                to_idx = grid[i + 1][j]
                if from_idx != to_idx + 1 and from_idx + 1 != to_idx:
                    contacts.append((from_idx, to_idx))
            
            # check bottom neighbor
            if grid[i][j + 1] != None:
                to_idx = grid[i][j + 1]
                if from_idx != to_idx + 1 and from_idx + 1 != to_idx:
                    contacts.append((from_idx, to_idx))

    # no contacts at all? (besides direct contact)
    if not contacts:
        return

    # already had a similar folding? (same contact points)
    if tuple(contacts) in visited:
        return
    visited.add(tuple(contacts))

    # for each protein check whether more hydrophobic contacts exist
    for protein in best:
        # at least all direct contacts
        found = direct[protein]

        # can't beat the previous record?
        if found + len(contacts) <= best[protein]:
            continue

        # count other contact points
        for contactMask in contacts:
            # are both neighbors hydrophobic?
            if protein[contactMask[0]] == 'H' and protein[contactMask[1]] == 'H':
                found += 1

        # better than before?
        if best[protein] < found:
            best[protein] = found

# generate recursively all possible layouts
def search(current, grid, x, y):
    # protein completely placed on grid?
    if current == length:
        # don't check layouts mirrored along y-axis
        if y >= Center:
            optimize(grid)
        return

    # try all possible continuations
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == None:
            grid[nx][ny] = current
            search(current + 1, grid, nx, ny)
            grid[nx][ny] = None

# operate on a 30x30 grid, each protein starts at (Center, Center)
GridSize = 30
Center = GridSize // 2

# keep track of past contact points sequences (detect duplicates / strong similarities)
visited = set()
length = 15

# allocate memory
direct = {} # number of direct contacts between immediate neighbors (minimum value, independent of folding)
best = {} # optimized number of hydrophobic contacts per protein
mirror = set()

# count direct neighboring hydrophobic elements in each protein
for protein in itertools.product('HP',repeat=length):
    # The string backward has the same configuration
    reverse_string = protein[::-1]
    if reverse_string in best:
        mirror.add(protein)
        continue
    
    direct[protein] = 0
    for i in range(length - 1):
        if protein[i] == 'H' and protein[i+1] == 'H':
            direct[protein] += 1
    best[protein] = direct[protein]

# create an None grid
grid = [[None for _ in range(GridSize)] for _ in range(GridSize)]

# always start in the middle
x, y = Center, Center
grid[x][y] = 0

# due to symmetries I can also place the second element
x += 1
grid[x][y] = 1

# generate all layouts and then call optimize()
search(2, grid, x, y)

# count optimized contact points
ans = sum(best.values())

for protein in mirror:
    ans += best[protein[::-1]]
    
ans /= 2**length
print(ans)