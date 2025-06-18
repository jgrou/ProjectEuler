# https://oeis.org/A181688
limit = 10**12
MOD = 10**8

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
            ret[i + j - len(b) + 1] = (ret[i + j - len(b) + 1] - ret[i] * b[j])%MOD
    return ret[:len(b) - 1]

def kitamasa(c, a, n):
    d = [1]         # result poly
    xn = [0, 1]     # x^1
    f = [(-ci)%MOD for ci in c] + [1]  # f(x) = x^k - sum c_i x^i
    while n:
        if n & 1:
            d = poly_div(poly_mul(d, xn), f)
        xn = poly_div(poly_mul(xn, xn), f)
        n >>= 1
    return sum((ai * di)%MOD for ai, di in zip(a, d)) % MOD

a = [0,1,1,4]
c = [1,-2,2,2]
ans = kitamasa(c,a,limit)
print(ans)
