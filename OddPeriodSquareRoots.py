ans = 0

for N in range(1,10001):
    if N**0.5 % 1 !=0: # Check if N is not a square
        a0 = int(N**0.5)
        den = a0
        num = 1
        sequence = []
        First = True

        while First or num != 1.0:
            num = (N - den**2) / num
            a = int( (N**0.5 + den) / num)
            den = num * a - den
            sequence.append(a)
            First = False
    
        if len(sequence)%2==1:
            ans += 1