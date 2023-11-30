n = 10**12    
red = 6
blue = 15

while red+blue < n:
    red = 2 * blue + red - 1
    blue = blue + 2 * red