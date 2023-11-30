import math

ans = 0

for n in range(10, 7 * math.factorial(9)):
    SumOfFactorial = 0
    for i in str(n):
        SumOfFactorial += math.factorial(int(i))
    if SumOfFactorial == n:
        ans += n