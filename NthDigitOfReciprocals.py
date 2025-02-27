n = 10**7
s = 0

# First do primes necessary for euler totient to speed up
limit = int(n**0.5)
IsPrime = (limit + 1) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
            
Primes = [p for p in range(2,limit+1) if IsPrime[p]]

def euler_totient_product(n) :
    result = n   # Initialize result as n
      
  # Iterate through all prime factors of n
    for p in Primes:
        # Check if p is a prime factor.
        if n % p == 0 :
 
            # If yes, then update n and result
            while n % p == 0 :
                n //= p
            result = result * (1.0 - (1.0 / float(p)))
         
   # If n is prime
    if n > 1 :
        result -= result // n
    return int(result)

for k in range(2, n+1): # k=1 always gives 0
    x = k
    count2, count5 = 0, 0
    while x&1 == 0:
        x //= 2
        count2 += 1
    while x%5==0:
        x//= 5
        count5 += 1
    if x > 1:
        m = max(count2, count5) # After this many digits, there starts a repetition
        phi = euler_totient_product(x) # This is the length of the repition
        power = (n-m) % phi
        if power == 0:
            power += phi
        power += m
        d = int((10**power // k) % 10)
        s += d
        #print(k,d)
    
print(s)