n = 10**25

# Count the number of zeros between each two 1's
zeros = []
consecutive = 0

while n > 0:
    if n & 1 == 0: # Checks if n is odd
        consecutive += 1
    else:
        zeros.insert(0, consecutive)
        consecutive = 0
    n >>= 1 # divides the value of x by 2 (truncating any remainder) by performing a bitwise right shift operation
    
result = 1
sum_val = 1
for i in range(len(zeros)):
    result += zeros[i] * sum_val
    sum_val += result

print(result)