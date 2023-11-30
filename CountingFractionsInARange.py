fractions = []

def reduce_fraction(numerator, denominator):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Find the GCD
    common_divisor = gcd(numerator, denominator)

    # Reduce the fraction
    reduced_numerator = numerator // common_divisor
    reduced_denominator = denominator // common_divisor

    return reduced_numerator, reduced_denominator

for d in range(2, 12001):
    n = int(d/3) + 1
    
    while n/d < 1/2:
        fractions.append(reduce_fraction(n, d))
        n+=1
        
ans = len(set(fractions))