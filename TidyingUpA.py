import random
import itertools
import math

limit = 7
ans = 0
count1 = 0
max_segments = (limit+1)//2

def M(order):
    s = set()
    segments = 0
    maximum = 0
    
    for n in order:
        if n-1 in s and n+1 in s:
            segments -= 1
        if n-1 not in s and n+1 not in s:
            segments += 1
            maximum = max(segments, maximum)
        s.add(n)
        if maximum == max_segments:
            break
        
    return maximum

for order in itertools.permutations(range(1,limit+1),limit-1): # Last one doesn't matter: 5% faster
    m = M(order)
    ans += M(order)
    if m==2:
        count1+=1

ans /= math.factorial(limit)
print(count1)
# 1 occurs 2**(limit-1) times

#%% Random
N = math.factorial(limit)
x = list(range(1,limit+1))

for _ in range(N):
    random.shuffle(x)
    ans += M(x)
    
ans /= N