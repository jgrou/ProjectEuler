import math

num25 = {0:(0,0)}
n = 200_000
power = 12
num2 = 0
num5 = 0
ans = 0

# num25 is a dictionary with keys n and items(x,y) such that n! is x times divisible by 2 and y times divisible by 5
for j in range(1,n+1):
    i = j
    while i%2 == 0:
        i //= 2
        num2 += 1
    while i%5 == 0:
        i //= 5
        num5 += 1
    num25[j] = (num2,num5)
    
n25 = num25[n]
min_i = n //3 + 1 # i>j>k

for i in range(min_i, n+1):
    max_j = min(n-i, i)
    min_j = math.ceil((n-i)/2) # j>k=n-i-j
    for j in range(min_j, max_j+1):
        k = n - i - j
        
        result = tuple(n - x - y - z for n, x, y, z in zip(n25, num25[i], num25[j], num25[k]))
        div = min(result) # n! / (i!*j!*k!) is div times divisible by 10
        
        if div >= power:
            if i == j or j == k:
                ans += 3 # 3 options to order i,j,k
            else:
                ans += 6 # 6 options to order i,j,k