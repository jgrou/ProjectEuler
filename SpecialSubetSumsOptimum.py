NearOptimumSet = [20,31,38,39,40,42,45]

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
    if len(set(A)) != 7: # All elements have to be unique
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

def main():
    for i in range(len(NearOptimumSet)):
        for j in range(len(NearOptimumSet)):
            if i != j:
                for k in range(len(NearOptimumSet)):
                    if k !=j and k != i:
                        for l in range(len(NearOptimumSet)):
                            if l !=j and l != i and l != k:
                                for m in range(len(NearOptimumSet)):
                                    if m !=j and m != i and m != k and m!=l:
                                        PotentialSet = NearOptimumSet
                                        PotentialSet[i] += 1
                                        PotentialSet[j] += 1
                                        PotentialSet[k] -= 2
                                        #PotentialSet[l] -= 1
                                        #PotentialSet[m] -= 1
                                        if special(PotentialSet):
                                            print(PotentialSet)
                                            return True
    return False

SolutionFound = main()