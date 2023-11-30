import math

base_exp = []

with open('base_exp.txt') as f:
    for line in f:
        line = line.split(',')
        base_exp.append([int(x) for x in line])
        
def Greater(pair1, pair2): # Check if pair1 > pair2
    [x, n] = pair1
    [y, m] = pair2
    if n * math.log(x) > m * math.log(y):
        return True
    else:
        return False
    
maximum = base_exp[0]

for i in range(1, len(base_exp)):
    if Greater(base_exp[i], maximum):
        maximum = base_exp[i]
        ans = i