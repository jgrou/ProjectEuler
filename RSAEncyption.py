p = 19
q = 37
n = p * q
phi = (p-1)*(q-1)

IsPrime = (n+1) * [True]

for prime in range(2, int((n+1)**0.5)):
    if IsPrime[prime] == True:
        for k in range(prime**2, n+1, prime):
            IsPrime[k] = False

primes = [i for i in range(2,n+1) if IsPrime[i]]

# Find all possible e s.t. gcd(e,phi) = 1
IsE = (phi) * [True]
factorization ={}

for prime in primes:
    if phi%prime == 0:
        for k in range(prime, phi, prime):
            IsE[k] = False
        factorization[prime] = 0
        while phi%prime == 0:
            phi //= prime
            factorization[prime] += 1
        
    if phi == 1:
        break
   
phi = (p-1)*(q-1)         
E ={}
for i in range(2, phi):
    if IsE[i]:
        E[i] = None

minimum = n

for e in E.keys():
    unconcealed = 2 # 0 and 1 always
    for m in range(2,n):
        if pow(m,e,n) == m:
            #print(m)
            unconcealed += 1
            #if unconcealed > minimum:
            #    break
                
    E[e] = unconcealed
    if unconcealed < minimum:
        minimum = unconcealed
        
ans = 0
for key,value in E.items():
    if value == minimum:
        print(key)
        ans += key
        
# 12 * n + 11
# 12 * n + 87
# Becasue 12 = 3*4 which is the lcm of the powers of the factorization