MaxNumberOfConsecutivePrimes = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        prime = True
        n = 0
        while prime:
            number = n**2 + a * n + b
            if number < 2:
                prime = False
            else:
                for i in range(2, int(number**0.5 + 1)):
                    if number%i == 0:
                        prime = False
                        break
            n += 1
                
        if MaxNumberOfConsecutivePrimes < n:
            ans = a*b
            MaxNumberOfConsecutivePrimes = n
