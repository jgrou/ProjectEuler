# Generate random numbers
N = 1000
s = 500500 * [None]
t = 0
for k in range(500500):
    t = (615949 * t + 797807)%2**20
    s[k] = t - 2**19

Triangle = N *[None]
start = 0
for i in range(N):
    start += i
    Triangle[i] =  s[start:start+i+1]
 
ans = 0

# Iterate over all possible triangle starts
for row in range(N):
    for column in range(i+1):
        below = sum(Triangle[N-1][column:column+N-row]) # Bottom row corresponding to triangle starting at (row, column)
        for depth in range(N-row):
            value = sum(Triangle[N-2-depth][column:column+N-1-row-depth])
            
            if below < 0:
                value += below
            
            below = value
        if value < ans:
            ans = value