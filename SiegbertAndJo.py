# H = https://oeis.org/A139764
limit = 23416728348467685
from bisect import bisect_right

def Game(N):
    matrix = [[0], [0,1]]

    for total_pebbles in range(2, N+1):
        new_row = (total_pebbles + 1) * [0]
        new_row[total_pebbles] = 1 # Always win by taking all pebbles on first turn

        for i in range(1, total_pebbles // 3 + 1): # If I take more than one third other player wins next turn
            possibilities = matrix[total_pebbles-i][1:min(2*i, total_pebbles-i)+1]

            if sum(possibilities) == 0: # The other cannot win
                new_row[i] = 1

        matrix.append(new_row)
    return matrix

F = [1, 2]

while F[-1] <= limit:
    F.append(F[-2] + F[-1])

# DP for exact Fibonacci endpoints
S = {0: 0}
S[F[0]] = F[0]
S[F[1]] = F[0] + F[1]

for i in range(2, len(F)):
    S[F[i]] = S[F[i-1]] + F[i-1] + S[F[i-2]]

def pref(n):
    if n <= 0:
        return 0

    # if n is Fibonacci
    if n in S:
        return S[n]

    # largest Fibonacci < n
    i = bisect_right(F, n) - 1
    f = F[i]

    return S[f] + pref(n - f)

ans = pref(limit)
print(ans)