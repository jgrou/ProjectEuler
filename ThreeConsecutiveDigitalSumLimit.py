ans = 0
five = {}
ten = {}

def Helper(current, i):
    if i == 5:
        start = (current[0], current[1])
        end = (current[3],current[4])
        if start in five:
            if end in five[start]:
                five[start][end] += 1
            else:
                five[start][end] = 1
        else:
            five[start] = {}
            five[start][end] = 1
    else:
        for next_digit in range(10 - sum(current[i-2:i])):
            new = current.copy()
            new[i] = next_digit
            Helper(new, i+1)

for i1 in range(10):
    for i2 in range(10-i1):
        number = 10 * [None]        
        number = 5 * [None]
        number[0] = i1
        number[1] = i2
        Helper(number, 2)
        
for start1 in five:
    for end1 in five[start1]:
        for start2 in five:
            for end2 in five[start2]:
                if sum(end1) + start2[0] < 10 and end1[1] + sum(start2) < 10:
                    if start1 in ten:
                        if end2 in ten[start1]:
                            ten[start1][end2] += five[start1][end1] * five[start2][end2]
                        else:
                            ten[start1][end2] = five[start1][end1] * five[start2][end2]
                    else:
                        ten[start1] = {}
                        ten[start1][end2] = five[start1][end1] * five[start2][end2]
              
for start1 in ten:
    if start1[0] == 0: # Without any leading zeros
        continue
    for end1 in ten[start1]:
        for start2 in ten:
            for end2 in ten[start2]:
                if sum(end1) + start2[0] < 10 and end1[1] + sum(start2) < 10:
                    ans += ten[start1][end1] * ten[start2][end2]
