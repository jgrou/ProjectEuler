n = 7830457
modulus = 10**10
ans = 2

for i in range(1,n):
    ans = (ans * 2) % modulus
        
ans = (ans * 28433) % modulus
ans += 1