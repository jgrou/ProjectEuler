primes = []
minimum = 10**7

def Prime(n):
    for p in primes:
        if p > n**0.5:
            break
        if n % p == 0:
            return False
    return True

def euler_totient(n):
    phi = n  # Initialize phi with n
    
    # Iterate through primes to the square root of n
    for p in primes:
        if p > n**0.5:
            break
        if n % p == 0:
            # i is a prime factor of n
            while n % p == 0:
                n //= p
            phi -= phi // p
    
    # If n is still greater than 1, it must be a prime number
    if n > 1:
        phi -= phi // n
    
    return phi

def are_permutations(num1, num2):
    # Convert numbers to strings
    str1 = str(num1)
    str2 = str(num2)

    # Check if the lengths are equal
    if len(str1) != len(str2):
        return False

    # Create dictionaries to count digit occurrences
    count1 = {}
    count2 = {}

    # Count occurrences of digits in the first number
    for digit in str1:
        count1[digit] = count1.get(digit, 0) + 1

    # Count occurrences of digits in the second number
    for digit in str2:
        count2[digit] = count2.get(digit, 0) + 1

    # Compare the digit counts
    return count1 == count2

            
for n in range(2, 10**7):
    if Prime(n):
        phi = n-1
        primes.append(n)
    else:  
        phi = euler_totient(n)
    if are_permutations(n, phi):
        sol = n / phi
        if sol < minimum:
            minimum = sol
            ans = n