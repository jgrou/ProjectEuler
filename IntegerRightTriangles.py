ans = 0
MaxNoOfSolutions = 0

for p in range(1001):
    NoOfSolutions = 0
    for c in range(int(p/3), int(p/2)+1): # c can be at most half p by triangle inequality and at leats p/3 since it is the largest side
        for a in range(1,c):
            b = p-c-a
            if a**2 + b**2 == c**2:
                NoOfSolutions += 1
                break
    if NoOfSolutions > MaxNoOfSolutions:
        MaxNoOfSolutions = NoOfSolutions
        ans = p