ans = 0

for n in range(2, 9**5 * 6):
    SumOfFifthPowers = 0
    for i in range(len(str(n))):
        SumOfFifthPowers += float(str(n)[i])**5
    if SumOfFifthPowers == n:
        ans += n