lengths = [1]

for i in range(2,1000001):
    n = i
    LengthOfSequence = 0
    while n >= i:
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
            
        LengthOfSequence += 1
    
    lengths.append(LengthOfSequence + lengths[int(n)-1])