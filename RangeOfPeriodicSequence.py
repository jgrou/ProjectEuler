from scipy import optimize as opt
import numpy as np

def f(n,a):
    for _ in range(n):
        a = a - 1 / a
    return a
 
P = 25
accuracy = 8  # The answer changes constant with this
ans = 0
roots = set() # Keep track of which roots we already did, outside so if n is multiple of previous n, it does not find double

for n in range(2,P+1):
    print(n)
    root = lambda a: f(n,a) - a 
    X = np.linspace(0.0,1.0,2*n)  # It seems every range has at least one number below 1.0, so do something with linspace
    # Highly dependent on how fine our grid is
    
    for x0 in X[1:-1]: # Skip 0.0 and 1.0
        
        sol = opt.fsolve(root, x0)
        
        a = (n+1)* [None]
        a[0] = sol[0]

        for i in range(n):
            a[i+1] = a[i] - 1 / a[i]
        
        if round(a[0], accuracy) not in roots:
            print(a)
            diff = max(a) - min(a) 
            
            #if a[0] > 1000000*x0: # Then we hit a huge number which we should not take into account
            #    break
            
            ans += n * diff
            
            for ai in a:
                roots.add(round(ai, accuracy))
        
print(round(ans,4))