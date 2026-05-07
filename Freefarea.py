import copy

S = {'A', 'E', 'F', 'R'}
limit = 30
ans = 0

# Make matrix with rows the possible word endings: 4**3 and columns the possible states: (0,0,0,0)-(1,1,1,1) and dead
emptyMatrix = {}

for s1 in S:
    for s2 in S:
        for s3 in S:
            emptyMatrix[s1+s2+s3] = {}
            for count1 in ['0','1']:
                for count2 in ['0','1']:
                    for count3 in ['0','1']:
                        for count4 in ['0','1']:
                            emptyMatrix[s1+s2+s3][count1+count2+count3+count4] = 0
            emptyMatrix[s1+s2+s3]['death'] = 0

Matrix = copy.deepcopy(emptyMatrix)

for s1 in S:
    for s2 in S:
        for s3 in S:           
            Matrix[s1+s2+s3]['0000'] = 1

for i in range(3, limit):
    newMatrix = copy.deepcopy(emptyMatrix)
    for letter in S:
        for key, value in Matrix.items():
            new_word = key + letter
            new_key = new_word[-3:]
            
            for count_key, count_value in value.items():
                if new_word == 'FREE':
                    if count_key[0] == '0':
                        new_count_key = '1' + count_key[1:]
                    else:
                        new_count_key = 'death'
                elif new_word == 'FARE':
                    if count_key[1] == '0':
                        new_count_key = count_key[:1] + '1' + count_key[2:]
                    else:
                        new_count_key = 'death'
                elif new_word == 'AREA':
                    if count_key[2] == '0':
                        new_count_key = count_key[:2] + '1' + count_key[3:]
                    else:
                        new_count_key = 'death'
                elif new_word == 'REEF':
                    if count_key[3] == '0':
                        new_count_key = count_key[:3] + '1'
                    else:
                        new_count_key = 'death'
                else:
                    new_count_key = count_key

                newMatrix[new_key][new_count_key] += count_value

    Matrix = copy.deepcopy(newMatrix)

for s1 in S:
    for s2 in S:
        for s3 in S:           
            ans += Matrix[s1+s2+s3]['1111']

print(ans)