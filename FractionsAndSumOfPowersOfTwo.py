# gcd(123456789,987654321) = 9?!
import math
# https://oeis.org/A002487
# f(n) = a(n+1)
f = [1,1] # 0 and1 can be expressend 1 way

for n in range(2,242):
    binary = bin(n)[2:]
    # Start with the largest bit and see how many ways there are to write the rest
    pos = f[int(binary[1:],2)]
    
    # Now split the first bit, but if the next bit is 1, we need to split again
    while binary[:2] == '11':
        binary = binary[1:]

    if binary != '1': # If n = 2**k - 1 there is only 1 representation
        binary = '1' + binary[2:]
        pos += f[int(binary,2)]
    f.append(pos)

# An even number always has more possiblities than the odd number
for n in range(3,100,2):
    print(f[n],f[n-1])

# a(n+1) = (2 * floor(a(n-1)/a(n)) + 1 - a(n-1)/a(n)) * a(n)

def a(n):
    a, b = 1, 0
    while n > 0:
        if n & 1:
            b += a
        else:
            a += b
        n >>= 1
    return a,b
