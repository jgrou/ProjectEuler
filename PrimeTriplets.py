def T(n):
    return (n+1) * n //2

def neighbours(n):
    if n > T(Row+1):
        row = Row+2
    elif n > T(Row):
        row = Row+1
    elif n > T(Row-1):
        row = Row
    elif n > T(Row-2):
        row = Row-1
    else:
        row = Row-2
    yield n + row # There is always one below
    yield n + row + 1
    column = n - T(row-1)
    if column < row-1:
        yield n-row+2 # Right and above
    if column != row:
        yield n - row + 1 # One above
        yield n+1
    if column != 0:
        yield n-1 # One right
        yield n - row
        yield n+row-1

ans = 0
Row = 7208785
# A prime number is part of a prime triplet if it has two prime neighbors
# Of if it has a prime neighbour which has another prime neigbour
# So we need two rows below and two rows above
lower_limit = T(Row-3) + 1
upper_limit = T(Row+2)
prime_limit = int(upper_limit**0.5) + 1
IsPrime = (prime_limit + 1) * [True]
for p in range(2, int(prime_limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, prime_limit+1, p):
            IsPrime[k] = False
primes = [p for p in range(2,prime_limit+1) if IsPrime[p]]

is_prime = (upper_limit-lower_limit+1) * [True]
for p in primes:
    n = (lower_limit // p) * p
    if n < lower_limit:
        n += p
    while n <= upper_limit:
        is_prime[n - lower_limit] = False
        n += p

for p in range(T(Row-1)+1, T(Row)+1):
    if is_prime[p-lower_limit]:
        prime_neighbours = []
        for k in neighbours(p):
            if is_prime[k-lower_limit]:
                prime_neighbours.append(k)
        if len(prime_neighbours) > 1:
            ans += p
        elif len(prime_neighbours) == 1:
            new_p = prime_neighbours[0]
            prime_neighbours = []
            for k in neighbours(new_p):
                if is_prime[k-lower_limit]:
                    prime_neighbours.append(k)
            if len(prime_neighbours) > 1:
                ans += p

print(ans)
