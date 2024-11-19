limit = 1000
ans = 0

for i in range(0, limit, 3):
    ans += i

for i in range(0, limit, 5):
    ans += i
    
for i in range(0, limit, 15):
    ans -= i