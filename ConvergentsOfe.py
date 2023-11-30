N = 100

num = 1
k = int(N / 3)
if N % 3 == 0:
    den = 2 * k
else:
    den = 1
    
for j in reversed(range(N-2)):
    if j%3 == 1:
        old_den = den
        den = 2 * k * den + num
        num = old_den
        k -= 1
    else:
        old_den = den
        den = den + num
        num = old_den
    
num = 2 * den + num

ans = 0

for digit in str(num):
    ans += int(digit)