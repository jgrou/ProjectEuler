def IsPrime(n):
    for p in Primes:
        if n%p == 0:
            return False
        if p > n**0.5:
            break
    return True

def CountCombinations(Number, Minimal):
    if Number <= 2:
        return 1
    if Number in Primes:
        temp = 1
    else:
        temp = 0
    for i in Primes:
        if i >= Minimal and i <= int(Number/2):
            temp += CountCombinations(Number-i, i)
    return temp

searching = True
Primes = []
ans = 1

while searching:
    ans += 1
    prime = IsPrime(ans)
    if prime:
        Primes.append(ans)
    NoOfCombinations = CountCombinations(ans, 1)
    if prime:
        NoOfCombinations -= 1
    if NoOfCombinations > 5000:
        searching = False