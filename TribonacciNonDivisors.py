def TribonacciDivisor(n):
    T1, T2, T3 = 1, 1, 3
    while not T1 == T2 == T3 == 1:
        T1, T2, T3 = T2, T3, (T1+T2+T3)%n
        if T3 == 0:
            return True
    return False

count = 0
k = 3

while count < 124:
    k += 2
    if not TribonacciDivisor(k):
        count += 1