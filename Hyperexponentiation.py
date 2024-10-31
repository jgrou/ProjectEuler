def EulerTotientFunction(n):
    result = n   # Initialize result as n
      
    # Iterate through all prime factors of n
    p = 2
    while p * p <= n :
 
        # Check if p is a prime factor.
        if n % p == 0 :
 
            # If yes, then update n and result
            while n % p == 0 :
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
         
   # If n is prime
    if n > 1 :
        result -= result // n
    return int(result)

def power(x, n, mod):
    '''Calculate x**n modulo mod for large numbers with recursion'''
    res = x
    count = 1
    
    while res < mod and count < n:
        res *= x
        count += 1
        
    if count == n:
        return res % mod
    
    rest = n%count
    div = n // count
    
    return x**rest * power(res%mod, div, mod) % mod

a = 1777
b = 1855
Phi = b * [10**8]

for i in range(1,b):
    phi = EulerTotientFunction(Phi[i-1])
    Phi[i] = phi
    
start = len([x for x in Phi if x>1]) # A number modulo 1 is just 0
ans = 1

for i in range(start-1,0,-1):
    ans = power(a, ans, Phi[i-1])
    
print(ans)