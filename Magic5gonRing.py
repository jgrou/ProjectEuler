import itertools

permutations = list(itertools.permutations(range(1,11),10))
max_first_digit = 0
ans = 0

for permutation in permutations:
    if permutation[1] != 10 and permutation[2] != 10 and permutation[4] != 10 and permutation[6] != 10 and permutation[8] != 10: # 16 digits if 10 is outside
        if permutation[0] + permutation[1] == permutation[3] + permutation[4]:
            if permutation[2] + permutation[3] == permutation[5] + permutation[6]:
                if permutation[4] + permutation[5] == permutation[7] + permutation[8]:  
                    if permutation[6] + permutation[7] == permutation[9] + permutation[1]:
                        if permutation[8] + permutation[9] == permutation[0] + permutation[2]:
                            first_digit = min(permutation[0], permutation[3], permutation[5], permutation[7], permutation[9])
                            if first_digit >= max_first_digit:
                                start_position = permutation.index(first_digit)
                                if start_position == 0:
                                    SolutionSet = int(str(permutation[0]) + str(permutation[1]) + str(permutation[2]) + str(permutation[3]) + str(permutation[2]) + str(permutation[4]) + str(permutation[5]) + str(permutation[4]) + str(permutation[6]) + str(permutation[7]) + str(permutation[6]) + str(permutation[8]) + str(permutation[9]) + str(permutation[8]) + str(permutation[1]))
                                if start_position == 3:
                                    SolutionSet = int(str(permutation[3]) + str(permutation[2]) + str(permutation[4]) + str(permutation[5]) + str(permutation[4]) + str(permutation[6]) + str(permutation[7]) + str(permutation[6]) + str(permutation[8]) + str(permutation[9]) + str(permutation[8]) + str(permutation[1]) + str(permutation[0]) + str(permutation[1]) + str(permutation[2]))
                                if start_position == 5:
                                    SolutionSet = int(str(permutation[5]) + str(permutation[4]) + str(permutation[6]) + str(permutation[7]) + str(permutation[6]) + str(permutation[8]) + str(permutation[9]) + str(permutation[8]) + str(permutation[1]) + str(permutation[0]) + str(permutation[1]) + str(permutation[2]) + str(permutation[3]) + str(permutation[2]) + str(permutation[4]))
                                if start_position == 7:
                                    SolutionSet = int(str(permutation[7]) + str(permutation[6]) + str(permutation[8]) + str(permutation[9]) + str(permutation[8]) + str(permutation[1]) + str(permutation[0]) + str(permutation[1]) + str(permutation[2]) + str(permutation[3]) + str(permutation[2]) + str(permutation[4]) + str(permutation[5]) + str(permutation[4]) + str(permutation[6]))
                                if start_position == 9:
                                    SolutionSet = int(str(permutation[9]) + str(permutation[8]) + str(permutation[1]) + str(permutation[0]) + str(permutation[1]) + str(permutation[2]) + str(permutation[3]) + str(permutation[2]) + str(permutation[4]) + str(permutation[5]) + str(permutation[4]) + str(permutation[6]) + str(permutation[7]) + str(permutation[6]) + str(permutation[8]))
                                if SolutionSet > ans:
                                    max_first_digit = first_digit
                                    ans = SolutionSet