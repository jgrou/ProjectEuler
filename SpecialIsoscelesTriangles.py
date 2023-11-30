limit = 12
b = 2
SolutionsFound = 0
ans = 0

while SolutionsFound < limit:
    x = [5 * b**2 / 4 + 2 * b + 1, 5 * b**2 / 4 - 2 * b + 1]
    
    for h in x:
        if h > 0:
            L = round(h**0.5)
            if L**2 == h:
                SolutionsFound += 1
                ans += L
                print(L,b)
    b += 2