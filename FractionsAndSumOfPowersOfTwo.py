# https://oeis.org/A002487
f = [1,1] # 0 and 1 can be expressend 1 way

for n in range(2,3000):
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

# 0    vs 1     1 vs 1
# 10   vs 11:   2 vs 1
# 100  vs 101:  3 vs 2
# 1000 vs 1001: 4 vs 3

# 110  vs 111:  3 vs 1
# 1110 vs 1111: 4 vs 1

# 1100  vs 1101:  5 vs 3
# 11100 vs 11101: 7 vs 4

# 11000  vs 11001:   7 vs 5
# 111000 vs 111001: 10 vs 7
# (m,n) = n*m+1

# (k,l,m,n) = (k-1,l,m,n) + (1, l-1, m,n)
# if k = 1: (k-1,l,m,n) = (m,n)
# if l = 1: (1, l-1, m,n) = (m+1,n)
# (1,1,m,n):                          m*n+1 + n*(m+1)+1       = n*(2m+1)+2
# (2,1,m,n) = (1,1,m,n) + (m+1,n)   = n*(2m+1)+2 + (m+1)*n+1  = n*(3m+2)+3
# (3,1,m,n) = (2,1,m,n) + (m+1,n)   = n*(3m+2)+3 + (m+1)*n+1  = n*(4m+3)+4
# (1,2,m,n) = (m,n)     + (1,1,m,n) = m*n+1 + n*(2m+1)+2      = n*(3m+1)+3
# (1,3,m,n) = (m,n)     + (1,2,m,n) = m*n+1 + n*(3m+1)+3      = n*(4m+1)+4
# (2,2,m,n) = (1,2,m,n) + (1,1,m,n) = n*(3m+1)+3 + n*(2m+1)+2 = n*(5m+2)+5
# (3,2,m,n) = (2,2,m,n) + (1,1,m,n) = n*(5m+2)+5 + n*(2m+1)+2 = n*(7m+3)+7
# (n*m+1)*(K*L+1) + n*K

# (L,m,n) = (L-1,m,n) + (1,m-1,n)
# (1,1,n) = (n)     + (n+1)   = 2
# (2,1,n) = (1,1,n) + (n+1)   = 3
# (1,2,n) = (n)     + (1,1,n) = 3
# (2,2,n) = (1,2,n) + (1,1,n) = 5
# L*m+1
# From odd to even we go from (x1,x2,...,xk,l,m) to (x1,x2,...,xk,l,m-1,1) or (x1,x2,...,xk,l+1) if m=1

# even(x1,x2,...,xk,l) / even(x1,x2,...,xk,l,m-1,1) or
# even(x1,x2,...,xk,l) / even(x1,x2,...,xk,l+1)
# with even(x1,x2,...,xk,l) / even(x1,x2,...,xk,l+1) we cannot be less than 1/2 I think.

# (i,j,k,L,m,n) = (i-1,j,k,L,m,n) + (1,j-1,k,L,m,n)
# (1,1,k,L,m,n) = (k,L,m,n)     + (k+1,L,m,n)   = (n*m+1)*(K*L+1) + n*K + (n*m+1)*((K+1)*L+1) + n*(K+1)               = (n*m+1)*((2K+1)*L+2) + n*(2*K+1)
# (2,1,k,L,m,n) = (1,1,k,L,m,n) + (k+1,L,m,n)   = (n*m+1)*((2K+1)*L+2)+n*(2*K+1) + (n*m+1)*((K+1)*L+1) + n*(K+1)      = (n*m+1)*((3K+2)*L+3) + n*(3*K+2)
# (1,2,k,L,m,n) = (k,L,m,n)     + (1,1,k,L,m,n) = (n*m+1)*(K*L+1) + n*K + (n*m+1)*((2K+1)*L+2) + n*(2*K+1)            = (n*m+1)*((3K+1)*L+3) + n*(3*K+1)
# (2,2,k,L,m,n) = (1,2,k,L,m,n) + (1,1,k,L,m,n) = (n*m+1)*((3K+1)*L+3) + n*(3*K+1) + (n*m+1)*((2K+1)*L+2) + n*(2*K+1) = (n*m+1)*((5K+2)*L+5) + n*(5*K+2)
# (i*j+1) * [(n*m+1) * (K*L+1) + n*K] + (n*m+1)*i*L + n*i
#=(i*j+1) * (n*m+1) * (K*L+1) + (i*j+1)*n*K + (n*m+1)*i*L + n*i
#=(n*m+1)*[(i*j+1) * (K*L+1) + i*L] + n*[(i*j+1)*K + i]

# Guess for (g,h,i,j,k,l,m,n):
# (g*h+1) * [(n*m+1)*(i*j+1)*(K*L+1) + (n*m+1)*i*L + (i*j+1)*n*K + n*i] + g*j*[(n*m+1)*(K*L+1) + n*K] + g*l*(n*m+1) + g*n
#=(n*m+1) * [(g*h+1)*(i*j+1)*(K*L+1) + (g*h+1)*i*L + g*j*(K*L+1)+ g*l] + n*[(g*h+1)*(i*j+1)*K + (g*h+1)*i + g*j*K + g]

def even(BinExp):
    if len(BinExp) & 1:  # Odd number
        return even(BinExp[:-1])
    if len(BinExp) == 0:
        return 1
    res = (BinExp[0] * BinExp[1] + 1) * even(BinExp[2:])
    if len(BinExp) > 2:
        res += BinExp[0] * BinExp[-1]
    for i in range(3, len(BinExp)-2, 2):
        res += BinExp[0] * BinExp[i] * even(BinExp[i+1:])
    return res

def even2(BinExp):
    if len(BinExp) & 1:  # Odd number
        return even(BinExp[:-1])
    if len(BinExp) == 0:
        return 1
    res = (BinExp[-1] * BinExp[-2] + 1) * even(BinExp[:-2])
    if len(BinExp) > 2:
        res += BinExp[0] * BinExp[-1]
    for i in range(3, len(BinExp)-2, 2):
        res += BinExp[-1] * BinExp[i] * even(BinExp[:i])
    return res

def EvenWithFinal1(BinExp):
    if len(BinExp) == 0:
        return 1
    res = (BinExp[-2] + 1) * even(BinExp[:-2])
    if len(BinExp) > 2:
        res += BinExp[0]
    for i in range(3, len(BinExp)-2, 2):
        res += BinExp[i] * even(BinExp[:i])
    return res

# 87654321 / 123456789 = 13717421 / 109739369
# 109739369 = 13717421 * 8 + 1. So BinExp[-2] = 7
# BinExp[0] = 1
# L+1 = 13717421
# L = 13717421
# ans = 1,13717420,8
