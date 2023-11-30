x_max = 0

def RegularConvergents(N,n):
    a0 = int(N**0.5)
    den = a0
    num = 1
    sequence = []
    k = 0
    
    while k==0 or (num != 1.0 and k < n):
        num = (N - den**2) / num
        a = int( (N**0.5 + den) / num)
        den = num * a - den
        sequence.append(a)
        k+=1
        
    num = 1
    den = sequence[n%len(sequence) - 1]
        
    for i in reversed(range(n-1)):
        num, den = den, sequence[i%len(sequence)] * den + num
        
    return a0 * den + num, den

for D in range(1,1001):
    if (D**0.5)%1 != 0:
        x = int(D**0.5)
        y = 1
        n= 0
        
        while x**2 - D * y**2 != 1:
            n += 1
            x, y = RegularConvergents(D,n)
               
        if x > x_max:
            x_max = x
            ans = D