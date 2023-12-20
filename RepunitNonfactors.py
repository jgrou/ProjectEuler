def IsPrime(n):
    if n<2:
        return False
    for p in primes:
        if n%p == 0:
            return False
        if p > int(n**0.5):
            return True

def euler_totient(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    result = n  # Initialize result as n

    # Consider all prime factors of n and subtract their multiples from result
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            while n % prime == 0:
                n //= prime
            result -= result // prime

    # If n has a prime factor greater than its square root
    if n > 1:
        result -= result // n

    return result

def powmod(base, exponent, modulo):
    ''' Return base**exponenet mod modulo'''
    result = 1
    while exponent > 0:
        if exponent & 1: # Check if exponent is odd
            result = (result * base) % modulo
            
        base = (base * base) % modulo
        exponent >>= 1 # right shift assignment operator
    return result

limit = 100_000
primes = [2,3,5,7]
ans = 17

for p in range(11, limit):
    if IsPrime(p):
        primes.append(p)
        modulo = 9 * p
        phi = 6 * (p-1) # p is prime, so phi(9*p)= phi(9) * phi(p) 
        phi_of_phi = euler_totient(phi)
        stop = False
        
        # By Euler's totient rule, 10^(10^n) mod 9p = 10^m mod 9p with 
        # m = 10^n mod phi(9p) = 10^k mod phi(9p) with k = n mod phi(phi(9*p))
        
        for n in range(phi_of_phi):
            m = powmod(10,n,phi)
            if powmod(10,m,modulo) == 1: 
                stop = True
                break

        if not stop:
            ans += p