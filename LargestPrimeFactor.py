import math

N = 600851475143
p = 2

while p < math.sqrt(N):
    while N%p==0:
        N = N/p
    p+=1