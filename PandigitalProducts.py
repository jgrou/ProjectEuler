import math

PandigitalNumber = []
integers = [str(i) for i in range(1,10)]

for n in range(10000): # Impossible to write a five digit number as product of two two-digit numbers
    for i in range(1,int(math.sqrt(n))+1):
        if n%i ==0:
            string = str(n) + str(i) + str(int(n/i))
            if len(string) == 9:
                pandigital = True
                for j in integers:
                    if j not in string:
                        pandigital = False
                        break
                if pandigital and n not in PandigitalNumber:
                    PandigitalNumber.append(n)
                    
ans = sum(PandigitalNumber)