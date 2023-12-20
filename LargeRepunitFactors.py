def IsPrime(n):
    if n<2:
        return False
    for p in primes:
        if n%p == 0:
            return False
        if p > int(n**0.5):
            return True
    print('Not enough primes')

def powmod(base, exponent, modulo):
    result = 1
    while exponent > 0:
        if exponent & 1: # Check if exponent is odd
            result = (result * base) % modulo
            
        base = (base * base) % modulo
        exponent >>= 1 # right shift assignment operator
    return result

numFactors = 40
digits = 10**9
s = 0
primes = [2]
p=3

while numFactors > 0:
    if IsPrime(p):
        primes.append(p)
        modulo = (9*p)
        remainder = powmod(10, digits, modulo)
        if remainder == 1:
            s += p
            numFactors -= 1
    p += 1
        