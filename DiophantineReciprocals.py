primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] # Looked this up, feels like cheating
todo = {1: [0] * len(primes)}
  
while True:
    value = next(iter(todo))
    exponents = todo[value]
        
    del todo[value]
    
    # Number of solutions is the number of divisors of the square
    sol = 1
    for x in exponents:
        sol *= 2 * x + 1      
    sol = (sol + 1) / 2 # Only half of the solutions are unique
    
    if sol >= 4_000_000:
        break
        
    for i in range(len(exponents)):
        if exponents[i] == 1 and i > 3: # Also looked this up, feels like cheating
            break
        
        exponents = exponents.copy()  # Create a copy of exponents
        exponents[i] += 1
        
        value *= primes[i]
        todo[value] = exponents