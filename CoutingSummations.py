def CountCombinations(Number, Minimal):
    temp = 1
    if Number <= 1:
        return 1
    for i in range(1, int(Number/2)+1):
        if i >= Minimal:
            temp += CountCombinations(Number-i, i)
    return temp

ans = CountCombinations(61,1) - 1
print(ans)
