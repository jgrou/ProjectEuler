ans = 0

def euler_totient(n):
    phi = n  # Initialize phi with n
    
    # Iterate through primes to the square root of n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            phi -= phi // i
        i += 1
    
    # If n is still greater than 1, it must be a prime number
    if n > 1:
        phi -= phi // n
    
    return phi

for d in range(2, 1000001):
    ans += euler_totient(d)