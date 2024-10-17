N = 10**4
n = 0
s = (N+1) * [None]
ans = 0
k = 1
terms = 0

while n < N:
    binary = bin(k)
    
    ones = 0
    for digit in binary[2:]:
        if digit == '1':
            ones += 1
            if ones == 3:
                break
        else:
            ones = 0
    
    if ones != 3:
        n += 1
        s[n] = k
        if k & 1:
            ans += n**2
            terms += 1
    
    k += 1
  
#%% All numbers with three consecutive ones
three_consecutive_ones = set()
max_s = s[-1]
max_length = len(bin(max_s)) - 2

def f(bit_str):
    n = int(bit_str,2)
    if n > max_s:
        return
    three_consecutive_ones.add(n)
    
    f(bit_str + '0')
    f(bit_str + '1')
    
    for n_zeros in range(max_length - len(bit_str)):
        f('1' + n_zeros * '0' + bit_str)
    
f('111')

#%%
for i in range(1, s[-1]+1):
    if i in s and i in three_consecutive_ones:
        print('Double:',i)
    if i not in s and i not in three_consecutive_ones:
        print('Neither:',i)