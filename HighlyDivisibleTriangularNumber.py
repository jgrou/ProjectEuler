import math
N_triangle = 0
i = 1
N_divisors = 0

while N_divisors < 501:
    N_triangle += i
    i+=1
    
    if math.sqrt(N_triangle)%1==0: #Check if N_triangle is a square
        N_divisors = 1
    else:
        N_divisors = 0
    for j in range(1, int(math.sqrt(N_triangle))):
        if N_triangle%j==0:
            N_divisors+=2
    
    