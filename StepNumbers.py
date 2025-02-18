limit = 40  # Limit is the number of digits

# Make a list which stores for each starting digits and missing number (10*1024 possibilities) the number of occurences
# Store true/false as binary number 0-1023 use bitwise or '|'
cache = [1024*[0] for _ in range(10)]
ans = 0

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

    for i in range(1,10): # First digit cannot be 0
        ans += cache[i][-1]