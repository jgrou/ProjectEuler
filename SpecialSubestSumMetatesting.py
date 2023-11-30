def TestNeeded(s, t):
    if len(s) != len(t):
        return False
    if len(s) == 1:
        return False
    for k in range(len(s)):
        if s[k] > t[k]: # They are already sorted and min(s) < min(t)
            return True
    return False

A = [1,2,3,4,5,6,7,8,9,10,11,12]
possible_pairs = 0
ans = 0

def backtrack(start, subset):
    subsets.append(subset[:])
    
    for i in range(start, len(A)):
        subset.append(A[i])
        backtrack(i + 1, subset)
        subset.pop()

subsets = []
backtrack(0, [])
subsets = subsets[1:] # Exclude empty set

for i in range(len(subsets)):
    for j in range(i+1,len(subsets)):
        s = subsets[i]
        t = subsets[j]
        if set(s).isdisjoint(set(t)):
            possible_pairs += 1
            if TestNeeded(s, t):
                ans += 1