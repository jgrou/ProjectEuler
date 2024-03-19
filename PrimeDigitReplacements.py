from itertools import product

def Prime(n):
    for p in range(2, int(n**0.5+1)):
        if n%p==0:
            return False
    return True

def replace(locations, digit, number):
    number = str(number)
    for i, boolean in enumerate(locations):
        if boolean:
            number = number[:i] + digit + number[i+1:]
    return int(number)

def EnoughPrimes(family, Max):
    NumberOfNonPrimes = 0
    for number in family:
        if not Prime(number):
            NumberOfNonPrimes += 1
        if NumberOfNonPrimes == Max+1:
            return False
    return True
    
digits = [str(i) for i in range(10)]
combinations = list(product([False, True], repeat=5))[1:] # Remove all False

def main(x):
    while True:
        x += 1
    
        if Prime(x):
            for combination in combinations:
                if combination[0]:
                    family = [replace(combination, i, x) for i in digits[1:]] # If we replace the first digit we cannot choose 0.
                    if EnoughPrimes(family, 1):
                        return family[0]
                else:
                    family = [replace(combination, i, x) for i in digits]
                    if EnoughPrimes(family, 2):
                        return family[0]
                    
ans = main(10000)
