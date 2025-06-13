k = 4000
g = k * [1]

for k in range(2000,k):
    g[k] = g[k-2000] + g[k-1999]

def mat_mult(A, B, mod):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == 0:
                continue
            for j in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def mat_pow(A, power, mod):
    n = len(A)
    result = [[int(i == j) for j in range(n)] for i in range(n)]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, A, mod)
        A = mat_mult(A, A, mod)
        power //= 2
    return result

A = [2000 * [0] for _ in range(2000)] # Transition matrix to go the next state

for i in range(1999):
    A[i][i+1] = 1

A[-1][0] = 1
A[-1][1] = 1

# Example:
mod = 20092010
power = k - 1999
binary_rep = bin(power)[2:]
n_doubles = len(binary_rep)
powers_of_A = n_doubles * [None]
powers_of_A[0] = A  #A**(2**0) = A**1 = A

for i in range(1, n_doubles):
    powers_of_A[i] = mat_mult(powers_of_A[i-1], powers_of_A[i-1], mod)



# To find g[k] we need A**(k-1999) and multiply with [1,1,...,1] and find last item: i.e. sum of the last row
#result = mat_pow(A, k, mod)
