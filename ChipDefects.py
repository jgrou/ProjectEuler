import math

n = 1_000_000
k = 20_000

# Maybe we can represent a state as (a,b,c) where a denotes the number of chips with 0 defects,
# b the number of chips with 1 defect and c the number of chips with 2 defects
# Then make a dictionary with probability in that state
# We start at {(1_000_000,0,0):1}
# We have probability of a/1_000_000 to go from (a,b,c) to (a-1,b+1,c)
# We have probability of b/1_000_000 to go from (a,b,c) to (a,b-1,c+1)
# We have probability of c/1_000_000 to go a state with at least 3 defects which is not allowed

dic = {(n,0,0):1}

for error in range(k):
    new_dic = {}
    for (a,b,c), p in dic.items():
        if (a-1,b+1,c) in new_dic:
            new_dic[(a-1,b+1,c)] += p * a/n
        else:
            new_dic[(a-1,b+1,c)] = p * a/n
        if (a,b-1,c+1) in new_dic:
            new_dic[(a,b-1,c+1)] += p * b/n
        else:
            new_dic[(a,b-1,c+1)] = p * b/n
    dic = new_dic

ans = 1 - sum(dic.values())
print(round(ans,10))
