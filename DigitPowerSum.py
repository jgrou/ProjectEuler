def HasProperty(base, power):
    SumOfDigits = 0
    n = base**power
    for i in str(n):
        SumOfDigits += int(i)
    if SumOfDigits == base:
        return True, n
    return False, n

sequence = []

for k in range(2, 101):
    for p in range(2,9):
        boolean, number = HasProperty(k, p)
        if boolean:
            sequence.append(number)
            
sequence.sort()
ans = sequence[29]