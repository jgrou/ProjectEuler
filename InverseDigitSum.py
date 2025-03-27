def s(n):
    num_9s = n // 9
    first_digit = n % 9
    power_of_ten = pow(10, num_9s, modulo)  # 99...9 k times = 10**k - 1
    result = ((first_digit+1) * power_of_ten - 1) % modulo
    return result

def S(k):
    if k == 0:
        return 0
    
    # Number of full blocks of 9
    q = k // 9
    r = k % 9
    
    # Sum of complete blocks
    pow_10_q = pow(10, q, modulo)
    
    # Geometric sum part: 54 * (10^q - 1) / 9
    geometric_sum = 54 * (pow_10_q - 1) * pow(9, modulo - 2, modulo) % modulo
    
    # Subtract -9q for the block correction
    result = (geometric_sum - 9 * q) % modulo
    
    # Handle the remaining terms directly
    for n in range(9 * q + 1, k + 1):
        result = (result + s(n)) % modulo

    return result
        
modulo = 1_000_000_007 # This is prime
ans = 0
f0 = 0
f1 = 1

for i in range(2, 91):
    f1, f0 = f1+f0, f1
    ans = (ans + S(f1)) % modulo

print(ans)
