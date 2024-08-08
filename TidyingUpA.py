import random
import itertools
import math

limit = 10

#%%
ans = 0
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

#for order in itertools.permutations(range(1,limit+1),limit-1): # Last one doesn't matter: 5% faster
#    ans += M(order)

ans /= math.factorial(limit)
# 1 occurs 2**(limit-1) times

#%% Random
N = 10**6
x = list(range(1,limit+1))

for _ in range(N):
    random.shuffle(x)
    ans += M(x)
    
ans /= N

#%% Dynamic programming?
list_of_dictionaries = (limit+1) * [None]
list_of_dictionaries[0] = {0:1}
list_of_dictionaries[1] = {1:1}

for n in range(2,limit+1):
    dictionary ={}
    max_segments = (n+1)//2
    
    for i in range(1, max_segments+1):
        dictionary[i] = 0
    
    for last_piece in range(1,n+1):
        left_half = list_of_dictionaries[last_piece-1]
        right_half = list_of_dictionaries[n-last_piece]
        for left_key, left_item in left_half.items():
            for right_key, right_item in right_half.items():
                # This overestimates
                dictionary[left_key+right_key] += math.comb(n-1, last_piece-1) * left_item * right_item
                
    list_of_dictionaries[n] = dictionary