def Bouncy(n):
    number = str(n)
    increasing = True
    decreasing = True
    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            increasing = False
        if number[i] < number[i+1]:
            decreasing = False
    return not decreasing and not increasing

def main(N=19602, M=21781):
    while True:
        if Bouncy(M):
            N += 1
            if 100 * N == 99 * M:
                return M
        M += 1
        
ans = main()