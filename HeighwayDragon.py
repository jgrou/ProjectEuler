import math
# https://en.wikipedia.org/wiki/Dragon_curve
steps = 10**12
x = 0
y = 1
step = {}
max_i = int(math.log(steps,2))

for i in range(max_i):
    step[2**i] = (y, -x)
    x, y = x+y, y-x

diff = steps - 2**max_i
mirror = 1

while diff > 0:
    mirror_temp = 0
    while 2**i > diff:
        i-=1
        mirror_temp += 1
    x_step, y_step = step[2**i]
    x, y = x + mirror * y_step, y - mirror * x_step
    diff -= 2**i
    i-=1
    if mirror_temp > 0: # If we skip some values, then the direction changes
        mirror *= -1
    
print(x,y)
