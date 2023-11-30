def SumSquareDigits(k):
    return sum(int(i)**2 for i in str(k))

lst = []
MaxSquareDigitSum = 7 * 81

def function(x, n):
    while x >= n:
        x = SumSquareDigits(x)
        if x == 89:
            return True
        if x == 1:
            return False
    return x in lst

for n in range(1, MaxSquareDigitSum + 1):
    if function(n,n):
        lst.append(n)

ans = len(lst)

for n in range(MaxSquareDigitSum+1, 10_000_000):
    if SumSquareDigits(n) in lst:
        ans += 1