limit = 5000
IsPrime = limit * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit, p):
            IsPrime[k] = False

S = [p for p in range(2, limit) if IsPrime[p]]

def prime(n):
    for p in S:
        if p**2 > n:
            return True
        if n%p == 0:
            return False

pos = {2:1}  # Number of possibilities (value) to make prime number (key) with only 2

for p in S[1:]:
    new_pos = pos.copy()

    if p in new_pos:
        new_pos[p] += 1
    else:
        new_pos[p] = 1
    
    for key in pos:
        new_key = key + p

        if new_key in new_pos:
            new_pos[new_key] += pos[key]
        else:
            new_pos[new_key] = pos[key]

    pos = new_pos

ans = 0

for key, value in pos.items():
    if prime(key):
        ans += value

print(ans%10**16)
