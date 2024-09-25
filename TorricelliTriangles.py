lim = 25
values = set()

def sieve_of_eratosthenes(n):
    """Returns a list of all prime numbers up to n."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers

primes = sieve_of_eratosthenes(lim)

for c in primes: # 
    for b in range(int(c/3**0.5), c+1): #Angle of at most 120 degrees
        mina = max(1, 2/3**0.5 * c - b)
        for a in range(int(mina), b+1):
            x_C = (c**2 + b**2 - a**2) / (2 * c) # x coordinate of C, A is at (0,0) and B at (c,0)
            y_C = (b**2 - x_C**2)**0.5 # y coordinate of C
                
            # Find the point O which is in the middle down AB
            x_O = c / 2
            y_O = -3**0.5 * x_O
            
            dx = (a**2 - b**2) / (2 * c)
            dy = y_O - y_C
            
            CO = (dx**2 + dy**2)**0.5
            CO = round(CO, 10) # To avoid rounding errors
        
            if int(CO) == CO:
                print(a,b,c,CO)
                # If it holds for a,b,c then also for all multiples
                for i in range(1, lim // int(CO) + 1):
                    values.add(int(CO) * i)
                break # In practie we only find 1
        if int(CO) == CO:
            break