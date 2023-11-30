import itertools

def IsPrime(n):
    if n <2:
        return False
    if n == 2:
        return True
    if n%2==0:
        return False
    for p in range(3,int(n**0.5)+1,2):
        if n % p == 0:
            return False
    return True

def function(digits_left, PrimeSet=()):
    if digits_left == []:
        PandigitalPrimeSets.append(PrimeSet)
    for i in range(1, max(len(digits_left)+1,9)): # A number containing all digits is divisible by 3
        for item in list(itertools.permutations(digits_left, i)): 
            k = int(''.join(map(str, item)))
            if IsPrime(k):
                if len(PrimeSet) == 0 or PrimeSet[-1] < k: # Prevent double counting
                    new_digits = digits_left.copy()
                    for j in item:
                        new_digits.remove(j)
                    function(new_digits, PrimeSet + (k,))
    return

PandigitalPrimeSets = []
digits = [i for i in range(1,10)]
function(digits)