from scipy import optimize as opt
import numpy as np

def f(n,a):
    if n == 0:
        return a
    else:
        return f(n-1,a) - 1 / f(n-1,a)
 
P = 25
accuracy = 8
ans = 0
roots = set() # Keep track of which roots we already did, outside so if n is multiple if previousn, it does not find double

for n in range(2,P+1):
    print(n)
    root = lambda a: f(n,a) - a
    X = np.linspace(0.0,1.0,2*n)  # It seems every range has at least one number below 1.0, so do something with linspace
    
    for x0 in X[1:-1]: # Skip 0.0 and 1.0
        
        sol = opt.root(root, x0)
        
        a = (n+1)* [None]
        a[0] = sol.x[0]

        for i in range(n):
            a[i+1] = a[i] - 1 / a[i]
        
        if round(a[0], accuracy) not in roots:
            #print(a)
            diff = max(a) - min(a) 
            
            #if a[0] > 1000000*x0: # Then we hit a huge number which we should not take into account
            #    break
            
            ans += n * diff
            
            for ai in a:
                roots.add(round(ai, accuracy))
        
print(round(ans,4))