from scipy import optimize as opt
import numpy as np
from sympy import mobius, divisors

def N(n): 
    '''
    Likely, this formula below gives the number of solution for each n
    Each sequence consists of n numbers, so a(n)/n different sequences
    Still 1_342_176 sequences for 25
    OEIS A027375, A038199, A056267
    '''
    return sum(mobius(d) * 2**(n//d) for d in divisors(n))

def f(n,a):
    for _ in range(n):
        a = a - 1 / a
    return a
 
P = 10
accuracy = 5  # The answer changes constant with this

ans = 0
roots = set() # Keep track of which roots we already did, outside so if n is multiple of previous n, it does not find double

for n in range(2,P+1):
    Nsol = 0
    root = lambda a: f(n,a) - a 
    Nseq = int(N(n)) // n
    X = np.linspace(0.0,1.0, 21*Nseq+1)  # It seems every range has at least one number below 1.0, so do something with linspace
    # Highly dependent on how fine our grid is, until P=10, we need already this
    
    for x0 in X[1:-1]: # Skip 0.0 and 1.0
        sol = opt.fsolve(root, x0)
        
        a = (n+1)* [None]
        a[0] = sol[0]

        for i in range(n):
            a[i+1] = a[i] - 1 / a[i]
        
        if round(a[0], accuracy) not in roots:
            #print(a)
            Nsol += 1
            diff = max(a) - min(a) 
            
            #if a[0] > 1000000*x0: # Then we hit a huge number which we should not take into account
            #    break
            
            ans += n * diff
            
            for ai in a:
                roots.add(round(ai, accuracy))
    print(n, Nsol, Nseq)
    
print(round(ans,4))


