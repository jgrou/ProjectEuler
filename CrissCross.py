ans = 0 

for g11 in range(10):
    for g12 in range(10):
        for g13 in range(10):
            for g14 in range(10):
                s = g11 + g12 + g13 + g14 + g14
                maxg21 = min(s - g11, 9)
                ming21 = max(s - g11 - 2 * 9, 0) # Can add at most 2 times 9 after this
                for g21 in range(ming21, maxg21+1):
                    # Check bounds for second row, second column and diagonal
                    maxg22 = min(s - g12, s - g21, s - g11, 9)
                    ming22 = max(s - g12 - 2 * 9, s - g21- 2 * 9, s - g11 - 2*9, 0) 
                    for g22 in range(ming22, maxg22+1):
                        # Check bounds for second row, third column and anti-diagonal
                        maxg23 = min(s - g13, s - g21 - g22, s - g14, 9)
                        ming23 = max(s - g13 - 2 * 9, s - g21 - g22 - 9, s - g14 - 2*9, 0) 
                        for g23 in range(ming23, maxg23+1):
                            g24 = s - g21 - g22 - g23
                            if g24 > min(s - g14, 9):
                                continue
                            if g24 < max(s - g14 - 2 * 9, 0) :
                                continue
                            maxg31 = min(s - g11 - g21, 9)
                            ming31 = max(s - g11 - g21 - 9, 0)
                            for g31 in range(ming31, maxg31+1):
                                g41 = s - g11 - g21 - g31
                                if g41 < 0 or g41 > 9:
                                    continue
                                g32 = s - g14 - g23 - g41
                                if g32 < max(s - g31 - 2 * 9, s - g12 - g22 - 9, 0):
                                    continue
                                if g32 > min(s - g31, s - g12 - g22, 9): # Check if it is possible with diagonal
                                    continue
                                g42 = s - g12 - g22 - g32
                                if g42 > min(s - g41, 9):  # Check if g42 is possible with last row
                                    continue
                                if g42 < max(s - g41 - 2 * 9, 0):
                                    continue
                                # Check bounds for third row, third column and diagonal
                                maxg33 = min(s - g11 - g22, s - g31 - g32, s - g13 - g23, 9)
                                ming33 = min(s - g11 - g22 - 9, s - g31 - g32 - 9, s - g13 - g23 - 9, 0)
                                for g33 in range(ming33, maxg33+1):
                                    g34 = s - g31 - g32 - g33
                                    if g34 < 0 or g34 > 9:
                                        continue
                                    g43 = s - g13 - g23 - g33
                                    if g43 < 0 or g43 > 9:
                                        continue
                                    g44 = s - g11 - g22 - g33
                                    if g44 < 0 or g44 > 9:
                                        continue
                                    if g44 != s - g14 - g24 - g34:
                                        continue
                                    if g44 != s - g41 - g42 - g43:
                                        continue
                                    ans += 1