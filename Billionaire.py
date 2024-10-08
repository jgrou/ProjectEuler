import math

def ExpectedCapital(f, n_flips=1000, initial_captial=1.0):
    res = 0
    for n_heads in range(n_flips+1):
        capital = initial_captial
        n_tails = n_flips - n_heads
        
        if n_tails > n_heads:
            for flip in range(n_heads):
                capital *= (1.0 + 2 * f)
                capital *= (1.0 - f)
            for flip in range(n_heads, n_tails):
                capital *= (1 + 2 * f)
                if capital > 10**9:
                    break
        else:
            for flip in range(n_tails):
                capital *= (1.0 + 2 * f)
                capital *= (1.0 - f)
            for flip in range(n_tails, n_heads):
                capital *= (1 - f)
                if capital < 10**9:
                    break
                
        if capital >= 10**9:
            res += math.comb(n_flips, n_heads) 
    return res / 2**n_flips

# With a bit of guessing:
x = [0.01*i for i in range(101)]
y = [ExpectedCapital(xi) for xi in x]
ans = round(max(y),12) 