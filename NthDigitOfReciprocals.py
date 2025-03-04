n = 10**7
s = 0

for k in range(1, n+1):
    s += pow(10, n, 10 * k) // k  # Efficiently compute (10^n // k) % 10
    
print(s)