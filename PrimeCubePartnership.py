def IsPrime(n):
    if n<2:
        return False
    
    if n%2 == 0:
        return False
    
    for p in range(3, int(n**0.5)+1, 2):
        if n%p == 0:
            return False

    return True

p = 1
a = 1
FoundSolutions = 0
        
while p < 10**6:
    p = 3*a**2 + 3*a + 1
    if IsPrime(p):
        FoundSolutions += 1
    a += 1