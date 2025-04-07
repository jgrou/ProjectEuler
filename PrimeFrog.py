from fractions import Fraction

limit = 500
IsPrime = (limit + 1) * [True]
for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False

IsPrime[1] = False
sequence = 'PPPPNNPPPNPPNPN'

def P_prime(letter):
    if letter == 'P':
        return 2,3
    else:
        return 1,3

def P_not_prime(letter):
    if letter == 'P':
        return 1,3
    else:
        return 2,3

def Jump(pos, n=0, num=1, den=1, exp2=0):
    '''
    n: int: how manyth jump
    num, den: int: probability of this sequence num/den
    pos: int: number of the square the frog is on
    exp2: int: counts how many times we multiplied with 1/2
    '''
    if n == 15:
        yield Fraction(num, den * 2**exp2)
        return
    if pos == 1:
        p,q = P_not_prime(sequence[n])
        yield from Jump(2, n+1, num*p, den*q, exp2)
    elif pos == 500:
        p,q = P_not_prime(sequence[n])
        yield from Jump(499, n+1, num*p, den*q, exp2)
    else:
        if IsPrime[pos]:
            p,q = P_prime(sequence[n])
        else:
            p,q = P_not_prime(sequence[n])
        yield from Jump(pos+1, n+1, num*p, den*q, exp2+1)
        yield from Jump(pos-1, n+1, num*p, den*q, exp2+1)

ans = Fraction(0,1)
for start_pos in range(1, 501):
    for p in Jump(start_pos):
        ans += p

ans *= Fraction(1,500)
print(ans)
