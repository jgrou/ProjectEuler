q = 10000
p = 3
S = 10001 * [290797]
T = 10001 * [290797%3]

for i in range(q):
    S[i+1] = S[i]**2 % 50515093
    T[i+1] = S[i+1] % p
    
N = 0
mod = 3**20

for n in range(q+1):
    N += (T[n] * p**n) % mod