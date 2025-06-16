limit = 10**18
MOD = 20092010
 
def mod(x):
    x %= MOD
    return x + MOD if x < 0 else x

def poly_mul(a, b):
    ret = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            ret[i + j] = (ret[i + j] + a[i] * b[j]) % MOD
    return ret

def poly_div(a, b):
    ret = a[:]
    for i in range(len(ret)-1, len(b)-2,-1):
        for j in range(len(b)):
            ret[i + j - len(b) + 1] = mod(ret[i + j - len(b) + 1] - ret[i] * b[j])
    return ret[:len(b) - 1]

def kitamasa(c, a, n):
    d = [1]         # result poly
    xn = [0, 1]     # x^1
    f = [mod(-ci) for ci in c] + [1]  # f(x) = x^k - sum c_i x^i
    while n:
        if n & 1:
            d = poly_div(poly_mul(d, xn), f)
        xn = poly_div(poly_mul(xn, xn), f)
        n >>= 1
    return sum(mod(ai * di) for ai, di in zip(a, d)) % MOD

c = 2000 * [0]
c[0] = 1
c[1] = 1
a = 2000 * [1]

ans = kitamasa(c,a,limit)
print(ans)
