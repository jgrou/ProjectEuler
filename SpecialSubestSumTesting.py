def find_subsets(nums):
    def backtrack(start, subset):
        subsets.append(subset[:])
        
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
    
    subsets = []
    backtrack(0, [])
    return subsets

def special(A):
    subsets = find_subsets(A)
    if len(set(A)) != len(A): # All elements have to be unique
        return False
    for s in subsets:
        for t in subsets:
            if t != s:
                if sum(s) == sum(t):
                    return False
            if len(s) > len(t):
                if sum(s) <= sum(t):
                    return False
                
    return True

ans = 0

with open('sets.txt') as f:
    for line in f:
        number = line.strip().split(',')
        sets = ([int(i) for i in number])
        if special(sets):
            ans += sum(sets)
