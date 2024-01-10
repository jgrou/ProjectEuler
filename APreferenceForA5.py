def NextPaths(path):
    '''
    Given a path, return all possible paths in the next turn
    A path is represented as the number of sheets of each size, 
    the probability of the path and 
    the number of times the supervisor has found a single sheet so far
    '''
    A2,A3,A4,A5,p,count = path
    total_paper = A2 + A3 + A4 + A5
    if total_paper == 1:
        count += 1
    paths = []
    
    if A2 > 0:
        p2 = p * A2 / total_paper
        paths.append((A2-1, A3+1, A4+1, A5+1, p2, count))
    if A3 > 0:
        p3 = p * A3 / total_paper
        paths.append((A2, A3-1, A4+1, A5+1, p3, count))
    if A4 > 0:
        p4 = p * A4 / total_paper
        paths.append((A2, A3, A4-1, A5+1, p4, count))
    if A5 > 0:
        p5 = p * A5 / total_paper
        paths.append((A2, A3, A4, A5-1, p5, count))
    
    return paths

start_paths = [(1,1,1,1,1,0)]  # Start with one sheet of each size with probability 1 and 0 times found a single sheet

# Calculate all possible paths
for _ in range(14):
    new_paths = []
    for path in start_paths:
        new_paths.extend(NextPaths(path))
    start_paths = new_paths
 
ans = 0
p=0
for final_path in new_paths:
    p += final_path[4] 
    ans += final_path[4] * final_path[5]
    
ans = round(ans,6)