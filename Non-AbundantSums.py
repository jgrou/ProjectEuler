AbundantNumbers = []
NonAbundantSum = NonAbundantSum = [i for i in range(1,24)]

for n in range(1,28123):
    SumOfDivisors = 0
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            SumOfDivisors += i
    if SumOfDivisors > n:
        AbundantNumbers.append(n)
        
for n in range(25,28124):
    AbundantSum = False
    for a in [a for a in AbundantNumbers if a<= n/2]:
        if n-a in AbundantNumbers:
            AbundantSum = True
            break
    if AbundantSum == False:
        NonAbundantSum.append(n)
        
ans = sum(NonAbundantSum)