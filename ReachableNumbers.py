class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator,
                        self.denominator * other.numerator)

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __hash__(self):
        return hash((self.numerator, self.denominator))
    
# First generate all possible number cominations s.t. 1 through 9 are used exactly once in that order
string = '123456789'
q = { 1: [[1]] }

def decompose(n):
    '''Generate partitions, but also all orders'''
    try:
        return q[n]
    except:
        pass

    result = [[n]]

    for i in range(1, n):
        a = n-i
        R = decompose(i)
        for r in R:
            result.append([a] + r)

    q[n] = result
    return result

def numbers(partition):
    '''Transform a partition of the number 9 to a partition of the string 123456789'''
    result = ()
    start = 0
    for digit in partition:
        result += (Fraction(int(string[start:start+digit])),)
        start += digit
    return result

number_combinations = []

for partition in decompose(9):
    number_combinations.append(numbers(partition))
    
# Not take all possible arithmetic operations for each number combination
def add(a,b):
    return a + b

def subtract(a,b):
    return a + Fraction(-b.numerator, b.denominator)

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

operations = [add, subtract, multiply, divide]

def possibilities(partitions):
    new_partitions = set()
    
    for partition in partitions:
        for i in range(len(partition)-1): # i is the position of the first number we take an operation on
            for operation in operations:
                if operation != divide or partition[i+1].numerator != 0: # Prevent division by 0
                    new_partitions.add(partition[:i] + (operation(partition[i], partition[i+1]),) + partition[i+2:])
                
    return new_partitions
  
final_set = set()
      
for combination in number_combinations:
    set_of_partitions = {combination}
    
    for _ in range(len(combination) - 1):
        set_of_partitions = possibilities(set_of_partitions)
        
    for number in set_of_partitions:
        number = number[0] # Make tuple into number
        if number.denominator < 0:
            number.numerator *= -1
            number.denominator *= -1
        if number.numerator <= 0:
            continue
        if number.numerator % number.denominator == 0:
            final_set.add(number.numerator // number.denominator)

ans = sum(final_set)