def ndiv(n):
    """
    Function to count the number of divisors of a given number.
    
    Parameters:
    n (int): The number for which divisors are counted.

    Returns:
    int: The number of divisors of n.
    """
    if n <= 0:
        return 0  # No divisors for non-positive integers

    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1  # Perfect square
            else:
                count += 2  # Both i and n/i are divisors
    return count

limit = 1000
ans = 0
dT = (limit+1)*[None]
dT[1] = 1

for k in range(2,limit+1):
    dT[k] = ndiv(k*(k+1)//2)
    
for i in range(1, limit-1):
    for j in range(i+1, limit):
        if dT[i] > dT[j]:
            for k in range(j+1, limit+1):
                if dT[j] > dT[k]:
                    ans += 1
                    
print(ans)