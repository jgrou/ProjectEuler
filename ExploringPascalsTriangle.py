N = 10**9
total_entries = N * (N + 1) // 2

# Check the largest power of 7 which is below N
k = 1 

while 7**k <= N:
    k += 1

# Store dictionary with values of powers of 7
values = {} 
values[7] = 0
old_power = 7
        
for i in range(2, k):
    power = 7**i
    values[power] = 7 * 6 * old_power * (old_power-1) // 4 + 7 * 8 * values[old_power] // 2 # 7 layers of 7**i until 7**(i+1)
    old_power = power

# Count of the zeros
zeros = 0 
multiplication_factor = 1

for i in range(k-1, 0, -1):
    power = 7**i
    n = N // power # Number of times the power fits in N
    
    zeros += multiplication_factor * (n * (n-1) * power * (power - 1) // 4 + n * (n+1) * values[power] // 2) # Number of zeros until n * 7**i
        
    N -= n * power # Number of rows left
    until_next = power - N # Number of rows until (n+1) * 7**i
        
    # The last row is crossed somewhere, with n+1 triangles of smaller order and n triangles of zeros in between
    zeros += multiplication_factor * n * (power * (power - 1) - until_next * (until_next - 1)) // 2 # Number of zeros in between
    multiplication_factor *= (n + 1)  # Number of triangles of one order smaller in the bottom row
    
answer = total_entries - zeros