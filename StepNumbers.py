limit = 21  # Limit is the number of digits

#%% Brute force
StepNumbers = set()

def StepNumber(current=(), i=0, last=None):
    if i == 0:
        for j in [1,2,3,4,9]:
            StepNumber(current+(j,), i+1, j)
    elif i == limit:
        StepNumbers.add(current)
        return
    else:
        if last == 9:
            new = [8]
        elif last == 0:
            new = [1]
        else:
            new = [last-1, last+1]
        for j in new:
            StepNumber(current+(j,), i+1, j)
            
StepNumber()

# Check if pandigital
ans = 0

for n in StepNumbers:
    if len(set(n)) == 10:
        if n[0] == 9:
            ans += 1
        else:
            ans += 2
            
#%% Make a list which stores for each starting digits and missing number (10*1024 possibilities) the number of occurences
# Store true/false as binary number 0-1023 use bitwise or '|'
cache = [1024*[0] for _ in range(10)]

for i in range(10):
    key = 2**i
    cache[i][key] = 1
    
for _ in range(limit-1):
    new_cache = [1024*[0] for _ in range(10)]
    for i in range(10):
        for previous in range(1024):
            if i != 0:
                new_cache[i][previous | 2**i] += cache[i-1][previous]
            if i != 9:
                new_cache[i][previous | 2**i] += cache[i+1][previous]
    cache = new_cache
    
ans2 = 0

for i in range(1,10): # First digit cannot be 0
    ans2 += cache[i][-1]