NumberOfDigits = 100
ans = 0
factorial = 1

for n in range(1, NumberOfDigits+1):
    factorial *= n
    increasing = 1
    decreasing = 1
    for i in range(n):
        increasing *= (9+i)
        decreasing *= (9+i+1)
    ans += (increasing + decreasing) // factorial - 10 # Minus the doubles and 1 