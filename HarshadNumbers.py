def Prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    for k in range(3, int(n**0.5)+1,2):
        if n%k==0:
            return False
    return True

# Find all strong right truncatable Harshad numbers by iteratively building from the previous nubmers
RightTruncatableHarshad = {1:set(range(1,10))}
StrongRightTruncatableHarshad = set()

for NoOfDigits in range(2, 14):
    new_set = set()
    for m in RightTruncatableHarshad[NoOfDigits-1]: # Right truncatable Harshad numbers with one digit less
        for new_digit in range(10):
            n = 10*m + new_digit
            SumOfDigits = sum(int(i) for i in str(n))
            if not(n%SumOfDigits): # Harshad
                new_set.add(n)
                if Prime(n // SumOfDigits): # Strong Harshad
                    StrongRightTruncatableHarshad.add(n)
    RightTruncatableHarshad[NoOfDigits] = new_set
    
ans = 0

for n in StrongRightTruncatableHarshad:
    for last_digit in ['1','3','7','9']: # Possible last digits of a prime
        m = int(str(n)+last_digit)
        if Prime(m):
            ans += m