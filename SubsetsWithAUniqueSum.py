limit = 20
k = limit//2
  
#%% Brute force
A = [i**2 for i in range(1,limit+1)]
res = {}
stop = len(A)-k+1
ans = 0

def FindSubset(subset, j, start):
    if j ==k:
        yield sum(subset)
        return
        
    for i in range(start, stop+j):
        subset.add(A[i])
        yield from FindSubset(subset, j+1, i+1)
        subset.remove(A[i])

for s in FindSubset(set(), 0, 0):
    if s in res:
        res[s] += 1
    else:
        res[s] = 1
        
for s in res:
    if res[s] == 1:
        ans += s

#%% Recursion: this is actually slower
SquareSums = [{} for _ in range(k+1)]

def f(n_elements=1, start=1, square_sum=0, tup=tuple()):
    if n_elements == k+1:
        return
    
    for i in range(start,limit+1):
        new_square_sum = square_sum + i**2
        new_tup = tup + (i,)
        if new_square_sum in SquareSums[n_elements]:
            SquareSums[n_elements][new_square_sum].add(new_tup)
        else:
            SquareSums[n_elements][new_square_sum] = {new_tup}

        f(n_elements+1, i+1, new_square_sum, new_tup)
    
f()

ans2 = 0

for key in SquareSums[k]:
    if len(SquareSums[k][key]) > 1:
        continue
    ans2 += key