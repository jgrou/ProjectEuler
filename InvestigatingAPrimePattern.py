def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    return [num for num in range(2, n + 1) if primes[num]]

def IsPrime(n_max,n1,n3,n7,n9,n13,n27): # check primality of all 6 numbers at the same time, much faster
    condition5 = False
    condition11 = False
    condition15 = False
    condition17 = False
    condition19 = False
    condition21 = False
    condition23 = False
    condition25 = False
    for p in primes:
        if p > n_max:
            break
        if n1%p == 0:
            return False
        if n3%p == 0:
            return False
        if (n3+2)%p == 0:
            condition5 = True # n^2 + 5 cannot be prime
        if n7%p == 0:
            return False
        if n9%p == 0:
            return False
        if (n9+2)%p == 0:
            condition11 = True # n^2 + 11 cannot be prime
        if n13%p == 0:
            return False
        if (n13+2)%p == 0:
            condition15 = True # n^2 + 15 cannot be prime
        if (n13+4)%p == 0:
            condition17 = True # n^2 + 17 cannot be prime
        if (n13+6)%p == 0:
            condition19 = True # n^2 + 19 cannot be prime
        if (n13+8)%p == 0:
            condition21 = True # n^2 + 21 cannot be prime
        if (n13+10)%p == 0:
            condition23 = True # n^2 + 23 cannot be prime
        if (n13+12)%p == 0:
            condition25 = True # n^2 + 25 cannot be prime
        if n27%p == 0:
            return False
    return condition5 and condition11 and condition15 and condition17 and condition19 and condition21 and condition23 and condition25


limit = 150_000_000
primes = sieve_of_eratosthenes(limit+27)
ans = 0

for k in range(1,15_000_000):
    n = 10*k # n should end in 0
    n1 = n**2 + 1
    n3 = n**2 + 3
    n7 = n**2 + 7
    n9 = n**2 + 9
    n13 = n**2 + 13
    n27 = n**2 + 27
    n_max = n27**0.5
    if IsPrime(n_max, n1, n3, n7, n9, n13, n27):
        ans += n
        print(n)