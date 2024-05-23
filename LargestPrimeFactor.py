N = 600851475143
p = 2

while p < N**0.5:
    while N%p==0:
        N = N/p
    p+=1