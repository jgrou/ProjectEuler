N = 5

all_zeros = N * (0,)
sequence = all_zeros + (1,) # Start with all zeros, next should be 1 otherwise we obtain again all zeros
ans = 0

# Make dictionary called subsequences where each key is a sequence and each value all possible subsequences of length 3
dic = {sequence: {all_zeros, (N-1) * (0,) + (1,)}}

for _ in range(N+1, 2**N):
    new_dic = {}
    
    for sequence in dic:
        last_part = sequence[1-N:]
        subsequences = dic[sequence]
        
        add_zero = last_part + (0,)
        add_one = last_part + (1,)
        
        if add_zero not in subsequences:
            new_dic[sequence + (0,)] = subsequences | {add_zero}
            
        if add_one not in subsequences:
            new_dic[sequence + (1,)] = subsequences | {add_one}
        
    dic = new_dic

for sequence in dic:
    subsequences = dic[sequence]
    
    # Add checks for the circle
    check1 = sequence[-4:] + sequence[:1]
    if check1 not in subsequences:
        check2 = sequence[-3:] + sequence[:2]
        if check2 not in subsequences:
            check3 = sequence[-2:] + sequence[:3]
            if check3 not in subsequences:
                check4 = sequence[-1:] + sequence[:4]
                if check4 not in subsequences:
            
                    number = 0
                    for i, digit in enumerate(sequence):
                        number += 2**(2**N-1-i) * digit
                    ans += number