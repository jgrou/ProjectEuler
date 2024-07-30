def ulam2(n):
    l = k - 4
    ul = n + 2
    st = 2**n + 1
    nxt = 2**n + 2**(n-1) + 1

    while l > 1:
        if nxt == st:
            per = k - 3 - l
            print(f"Ulam(2,{n}): Found quasiperiod of length {per}, spanning {ul-n}")

            q = l // per
            r = l % per
            ul = (q + 1) * (ul - n) + n
            if not r:  
               return ul
            ul += 2
            nxt |= 2**(n - 1) # bitwise or
            l = r
            continue

        # Check maximal a s.t. 2**(a-1) divides nxt
        a = 1
        while not nxt & 1: # Check if nxt is even
            a += 1
            nxt //= 2

        nxt //= 2 
        nxt ^= st # bitwise XOR: st = 10...01 with (n-1) 0's
        ul += 2*a
        l -= 1

    return ul

k = 100000000000
sum_val = 0

for n in range(5, 22, 2):
    ul = ulam2(n)
    sum_val += ul
    print(ul)

print(f"Sum: {sum_val}")