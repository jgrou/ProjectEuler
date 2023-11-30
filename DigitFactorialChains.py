import math

def DigitFactorial(n):
    sol = 0
    for i in str(n):
        sol += math.factorial(int(i))
    return sol

ans = 0

for n in range(1,10**6):
    lst = []
    while n not in lst:
        lst.append(n)
        n = DigitFactorial(n)
    if len(lst) == 60:
        ans += 1