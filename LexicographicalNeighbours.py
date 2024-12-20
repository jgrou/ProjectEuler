import math
   
def p(n):
    # Just consider n numbers: math.comb(26,n) possibilities
    # Split the set in i left and n-i right: math.comb(n,i) possibilities
    # Order each decreasing and glue together: if all largest number are in left not possible: so math.comb(n,i)-1
    res = 0
    for i in range(1,n):
        res += math.comb(n,i) - 1
    return res * math.comb(26,n)

n = 2
old_p = 0
new_p = p(n)

while new_p > old_p:
    n += 1
    old_p = new_p
    new_p = p(n)