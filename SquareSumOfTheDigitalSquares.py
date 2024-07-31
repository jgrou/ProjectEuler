import itertools
import math

squares = [i**2 for i in range(10)]
ans = 0

def CountOccurrencesAtEachPosition(partition):
    '''For a given partition [n1,n2,...] of 20, count how often the digit that occurs n1 times occurs at each position'''
    res = {}
    
    for i,n in enumerate(partition):
        new_partition = partition.copy()
        new_partition[i] -= 1
        possibilities = 1
        m = 19
        
        for k in new_partition:
            possibilities *= math.comb(m, k)
            m -= k
            
        res[n] = possibilities
        
    return res

# For each combination of 20 digits for which the sum of the squares is a square:
    # Count how often each unique digits occurs at every position
    # Add this n
    
for combination in itertools.combinations_with_replacement(squares, 20):
    s = sum(combination)
    if int(s**0.5)**2 == s:
        digits = [int(x**0.5) for x in combination]
        unique_digits = set(digits)
        counter = {}
        
        for digit in unique_digits:
            occurs = digits.count(digit)
            if occurs > 0:
                counter[digit] = occurs
        
        occurances = CountOccurrencesAtEachPosition(list(counter.values()))
        
        for k in unique_digits:
            ans += occurances[counter[k]] * int(9*str(k))
            ans %= 10**9