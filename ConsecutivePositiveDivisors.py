limit = 10**7

#%% Initial method
def CountDivisors(n):
    ans = 1
    for p in primes:
        if p**2 > n:
            break
        count = 0 # count how many times this prime occurs
        while n%p ==0:
            count += 1
            n //= p
        ans *= count+1
    return ans

# Only squares have an odd number of divisors
# Only primes have only 2 divisors
# n and n+1 cannot both be square or both prime (except 2 and 3)
# So both n and n+1 should not be prime or square
is_prime = [True] * (limit + 1)
is_square = [False] * (limit + 1)
p = 2
while p * p <= limit:
    if is_prime[p]:
        for i in range(p * p, limit + 1, p):
            is_prime[i] = False
    is_square[p*p] = True
    p += 1
    
primes = [p for p in range(2, limit + 1) if is_prime[p]]

ans = 1 # new == old, for n=2
new = CountDivisors(14) # 14 is first possibility
prev_wrong = False

for n in range(15, limit+1):
    wrong_n = is_square[n] or is_prime[n]
    
    if not wrong_n:
        new, old = CountDivisors(n), new
        if not prev_wrong and new == old:
                ans += 1
            
    prev_wrong = wrong_n # If this n is prime or square, the current and next we do not have to count
    
#%% Way quicker
ans = 0
divisors = [2] * (limit + 1) # Every number is divisible by 1 and itself

for i in range(2, int(limit**0.5) + 1):
    divisors[i**2] += 1 # Squares are divisible once
    for j in range(i**2 +i, limit+1, i): # All other numbers have 2 divisors for each divisor below sqrt(n)
        divisors[j] += 2
        
for i in range(2, limit):
    if divisors[i] == divisors[i+1]:
        ans += 1