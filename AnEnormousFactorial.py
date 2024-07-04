q = 10_000_000
p = 61
S = (q+1) * [290797]
T = (q+1) * [290797%p]

for i in range(q):
    S[i+1] = S[i]**2 % 50515093
    T[i+1] = S[i+1] % p
    
# Number of factors in a factorial is N//p + N//p**2 + ...
# That means T1 occurs once, T2 (1+p) times, etc.
# Sum 1+p+...+p**(n-1) = (1-p**n)/(1-p)
# p**n mod p**m = 0 if n>=m
x = 10
mod = p**x
ans = 0

for n in range(1, x):
    ans += (T[n] * ((p**n - 1) // (p-1)))
    ans %=mod
    
for n in range(x, q+1):
    ans += (T[n] * ((mod - 1) // (p-1)))
    ans %=mod