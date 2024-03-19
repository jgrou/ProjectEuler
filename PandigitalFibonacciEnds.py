import math

def Pandigital(x):
    for i in range(1,10):
        if str(i) not in str(x):
            return False
    return True
    
F1 = 1
F2 = 1
k = 2

while True:
    k += 1
    F2, F1 = F2 + F1, F2
    last_digits = F2 % 10**10
    if not Pandigital(last_digits):
        continue
    first_digits = F2 // 10**int(math.log10(F2) - 9)
    if Pandigital(first_digits):
        break
