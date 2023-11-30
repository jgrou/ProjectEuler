def isValidTriangle(oneSide, twoSides):
    check = 4 * twoSides * twoSides - oneSide * oneSide
    root = int(check**0.5)
    return root * root == check

N = 1_000_000_000
n_max = int((N+1)/3)
ans = 0

for n in range(5, n_max+1):
    if isValidTriangle(n+1,n):
        ans += 3*n+1
    if isValidTriangle(n-1,n):
        ans += 3*n-1

# Second faster but not proven method
plusOne = [1,5]
minusOne = [1,17]
solutions = [3 * plusOne[1] +1, 3 * minusOne[1] -1]

while solutions[-1] <= N + 3:
    nextPlusOne = 14 * plusOne[1] - plusOne[0] - 4
    nextMinusOne = 14 * minusOne[1] - minusOne[0] + 4
    
    plusOne[0] = plusOne[1]
    plusOne[1] = nextPlusOne
    minusOne[0] = minusOne[1]
    minusOne[1] = nextMinusOne
    
    solutions.append(3 * nextPlusOne + 1)
    solutions.append(3 * nextMinusOne - 1)

ans = 0

for x in solutions:
    if x <= N:
        ans += x