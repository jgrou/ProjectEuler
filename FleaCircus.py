N = 30
empty = [N * [1] for _ in range(N)]

for start_i in range(N):
    for start_j in range(N):
        # For each flea, check the probability where it ends up
        current = [N * [0] for _ in range(N)]
        current[start_i][start_j] = 1
        for ring in range(50):
            new_grid = [N * [0] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    p = current[i][j]
                    if i == N-1:
                        if j == N-1:
                            new_grid[N-2][N-1] += p/2
                            new_grid[N-1][N-2] += p/2
                        elif j == 0:
                            new_grid[N-2][0] += p/2
                            new_grid[N-1][1] += p/2
                        else:
                            new_grid[N-2][j] += p/3
                            new_grid[N-1][j-1] += p/3
                            new_grid[N-1][j+1] += p/3
                    elif i == 0:
                        if j == N-1:
                            new_grid[1][N-1] += p/2
                            new_grid[0][N-2] += p/2
                        elif j == 0:
                            new_grid[1][0] += p/2
                            new_grid[0][1] += p/2
                        else:
                            new_grid[1][j] += p/3
                            new_grid[0][j-1] += p/3
                            new_grid[0][j+1] += p/3
                    elif j == 0:
                        new_grid[i+1][0] += p/3
                        new_grid[i-1][0] += p/3
                        new_grid[i][1] += p/3
                    elif j == N-1:
                        new_grid[i+1][N-1] += p/3
                        new_grid[i-1][N-1] += p/3
                        new_grid[i][N-2] += p/3
                    else:
                        new_grid[i+1][j] += p/4
                        new_grid[i-1][j] += p/4
                        new_grid[i][j+1] += p/4
                        new_grid[i][j-1] += p/4
            current = new_grid
        # Now for each square, check the probability that it is empty
        for i in range(N):
            for j in range(N):
                empty[i][j] *= (1 - current[i][j])

ans = sum([sum(i) for i in empty])
print(round(ans,6))
