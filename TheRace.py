# I have to decide my best strategy if it is my turn
# If it is my turn, by definition I go first
r = 100
# TwoWins[i][j] is the probability that two wins if player 1 needs i points and player 2 j
TwoWins = [[0]*(r+1) for _ in range(r+1)]

for i in range(r+1):
    TwoWins[i][0] = 1 # If I need 0 points to win, I win

for i in range(1,r+1):
    for j in range(1,r+1):
        # Find best strategy
        best = 0
        T = 1
        while True:
            win2 = 0.5 / T # Probability I throw T heads
            lose2 = 1 - win2
            new_j = max(0, j - T)
            current = 0.5 * win2 * TwoWins[i-1][new_j] + 0.5 * win2 * TwoWins[i][new_j] + 0.5 * lose2 * TwoWins[i-1][j]
            current /= 1 - 0.5 * lose2 # Both players lose
            if current > best:
                best = current
            if new_j == 0:
                break
            T *= 2
            
        TwoWins[i][j] = best

# Since player 1 actually start, we have to take into account that he might throw heads immediately
ans = 0.5 * TwoWins[r][r] + 0.5 * TwoWins[r-1][r]
print(round(ans,8))
