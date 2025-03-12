import math

# Let x = 2**t, then solve quadratic equation
P_num = 0
P_den = 0
n = 0

while 12345 * P_num >= P_den:  
    n += 1  
    k = n * (n+1)  # k is of this form for D to be square
    D = 1 + 4*k
    x = (1 + D**0.5) // 2 
    t = math.log(x, 2)
    P_den += 1
    if 2**round(t) == x:
        P_num += 1