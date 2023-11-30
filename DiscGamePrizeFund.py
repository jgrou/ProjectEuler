import itertools

N = 15
BlueToWin = int(N/2) + 1
P_win = 0

def P_blue(i):
    return 1 / (1+i)
  
for NumOfBlues in range(BlueToWin, N+1):
    orders = list(itertools.combinations(range(1,N+1), NumOfBlues))
    for order in orders:
        p = 1
        for position in range(1,N+1):
            if position in order:
                p *= P_blue(position)
            else:
                p *= (1 - P_blue(position))
        P_win += p

ans = int(1/P_win)