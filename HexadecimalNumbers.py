N = 16

N1 = N**N - (N-1)**N
N1_or_2 = N**N - (N-2)**N

without_0 = 0
for n_digits in range(1, N+1):
    without_0 += (N-1)**n_digits
    
N0 = N**N - without_0

without_01 = 0
for n_digits in range(1, N+1):
    without_01 += (N-2)**n_digits
    
N0_or_1 = N**N - without_01
N0_and_1 = N0 + N1 - N0_or_1
N1_and_2 = 2 * N1 - N1_or_2

without_012 = 0
for n_digits in range(1, N+1):
    without_012 += (N-3)**n_digits
    
N0_or_1_or_2 = N**N - without_012
N0_and_1_and_2 = N0_or_1_or_2 - 2 * N1 - N0 + 2 * N0_and_1 + N1_and_2

digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def Hexadecimal(n):
    res = ''
    power = 0
    while 16**power < n:
        power += 1
    while power > 0:
        digit = n // 16**(power-1)
        res += digits[digit]
        n%= 16**(power-1)
        power -= 1
    return res

ans = Hexadecimal(N0_and_1_and_2)
print(ans)