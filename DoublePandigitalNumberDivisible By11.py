# sum(odd) – sum(even) must be divisible by 11.
# total_sum = 2 * sum(range(10))= 90
# sum(even) = 90 - sum(odd)
# 2 * sum(odd) - 90 must be divisible by 11
import itertools
import math

digits = (0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9)
ans = 0

for odd in set(itertools.combinations(digits, 10)):
    if abs(2*sum(odd) - 90)%11 == 0:
        orderings_odd = math.factorial(10)
        orderings_even = math.factorial(10)
        
        count_odd = 10 * [0]
        count_even = 10 * [0]
        for i in odd:
            count_odd[i] += 1
        for i in range(10):
            count_even[i] = 2 - count_odd[i]
            
        for i in range(10):
            orderings_odd //= math.factorial(count_odd[i])
            orderings_even //= math.factorial(count_even[i])

        ans += orderings_even * orderings_odd

ans = 9 * ans // 10 # Cannot start with 0
