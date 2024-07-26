MaxBlack = 3
MaxWhite = 1

previous = [(MaxWhite+1)*[0] for _ in range(MaxBlack+1)]
current = [(MaxWhite+1)*[0] for _ in range(MaxBlack+1)]

previous[0][0] = 1

# All possible subsets
for useBlack in range(MaxBlack+1):
    for useWhite in range(MaxWhite+1):
        if useBlack == 0 and useWhite == 0:
            continue
        
        # Put subset at every possible position
        for i in range(MaxBlack+1):
            for j in range(MaxWhite+1):
                current[i][j] = 0
                
                # Place it repeatedly
                k = 0
                while i >= k*useBlack and j >= k*useWhite:
                    current[i][j] += previous[i-k*useBlack][j-k*useWhite]
                    k+=1
              
        # Update previous
        for i in range(MaxBlack+1):
            for j in range(MaxWhite+1):
                previous[i][j] = current[i][j]
                
ans = current[MaxBlack][MaxWhite]