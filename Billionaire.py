import math
import matplotlib.pyplot as plt

def ExpectedCapital(f, n_flips=1000, initial_captial=1.0):
    res = 0
    for n_heads in range(n_flips+1):
        capital = (1+f)**n_heads * (1-f)**(n_flips - n_heads) * initial_captial
        if capital >= 10**9:
            res += math.comb(n_flips, n_heads) 
    return res / 2**n_flips

def function(f):
    return - ExpectedCapital(f)

x = [0.15 + i*0.001 for i in range(101)]
y = [ExpectedCapital(xi) for xi in x]
plt.plot(x,y)