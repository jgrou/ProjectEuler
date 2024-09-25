limit = 100
k = limit//2
ans = 0
   
# max_s[i][j] means the max sum you can achieve with i terms of at most j
max_s = [(limit+1) * [0] for _ in range(k+1)]

for i in range(k+1):
    for j in range(i,limit+1):
        max_s[i][j] = sum(m**2 for m in range((j-i)+1,j+1))
        
min_s = (k+1) * [0]

for j in range(1,k+1):
    min_s[j] = min_s[j-1] + j**2
    
def SetSum(s, n, max_i):
    global solution_count
    
    if solution_count > 1: # Stop recursion if more than one solution is already found
        return
    
    if s < min_s[n] or s > max_s[n][max_i]: # Not possible to make s anymore with remaining numbers
        return
    
    if n==0 and s==0: # We found a solution
        solution_count += 1
        if solution_count > 1:  # Stop early if 2nd solution is found
            return
    
    for j in range(n, max_i+1):
        SetSum(s-j**2, n-1, j-1)
        
for s in range(min_s[-1], max_s[-1][-1]+1):
    solution_count = 0
    SetSum(s, k, limit)
    
    if solution_count == 1:
        ans += s