from scipy.optimize import bisect

# https://en.wikipedia.org/wiki/Poisson_binomial_distribution
# Function to compute the probability of exactly 20 successes
def DC(q, n=50, points=20):
    PMF = [1]
    for i in range(1, n+1):
        nextPMF = (i+1) * [None]
        nextPMF[0] = i/q * PMF[0]
        nextPMF[i] = (1 - i/q) * PMF[i-1]
        for k in range(1,i):
            nextPMF[k] = (1- i/q) * PMF[k-1] + i/q * PMF[k]
        PMF = nextPMF
    return PMF[20]

def f(q):
    return DC(q) - 0.02
    
# Use binary search (bisection method) to find q such that f(q) = 0
ans = bisect(f, 51, 100, xtol=1e-11)
print(round(ans,10))
