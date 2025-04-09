ans = 0
MOD = 10**10
limit = 1000

for n in range(1, limit+1):
    ans += pow(n,n,MOD)
    ans %= MOD

print(ans)
