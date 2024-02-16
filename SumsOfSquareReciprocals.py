import math

# Found set of possible numbers online
possible_numbers = [2,3,4,5,6,7,8,9,10,12,13,14,15,18,20,21,24,28,30,35,36,39,40,42,45,52,56,60,63,70,72]
n = len(possible_numbers)

# Find least common multiple of the squared possible numbers
lcm = 1

for i in possible_numbers:
    lcm = lcm * i**2 // math.gcd(lcm, i**2)
    
# If we multiply every fraction by lcm, we need the denominators to add up to lcm/2
goal = lcm // 2

denominators = []

for i in possible_numbers:
    denominators.append(lcm // i**2)
    
# calculate maximum sum left if we add all numbers from that point on
sum_left = denominators.copy()

for i in range(n-1):
    sum_left[n-2-i] += sum_left[n-1-i]

# Brute force check for each fraction whether including them or not gives the correct result    
ans = 0

def check(to_go=goal, i=0):
    global ans 
    if to_go == 0:
        ans += 1 # If we have 0 to go, we have found a solution
        return
    if i < n:
        if to_go > sum_left[i] or to_go < 0:
            return # If we have more left than we can add or have added too much, we can stop
    
        check(to_go - denominators[i], i+1) # Include fraction i
        check(to_go, i+1) # Do not include fraction i
    return

check()