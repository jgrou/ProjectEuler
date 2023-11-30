import math

def Prime(n):
    for p in range(2,int(math.sqrt(n)+1)):
        if n%p==0:
            return False
    return True

diagonal = [1]
side_length = 1
primes = []
ratio = 1

while ratio >= 0.1:
    side_length += 2

    bottom_right = side_length**2
    bottom_left = bottom_right + 1 - side_length
    upper_left = bottom_left + 1 - side_length
    upper_right = upper_left + 1 - side_length
    
    numbers = [bottom_right, bottom_left, upper_left, upper_right]
    
    for i in numbers:
        diagonal.append(i)
        if Prime(i):
            primes.append(i)
    
    ratio = len(primes) / len(diagonal)