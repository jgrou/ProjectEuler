def Palindrome(number):
    number = str(number)
    for i in range(int(len(number)/2)+1):
        if number[i] != number[-i-1]:
            return False
    return True

def Lychrel(n):
    for _ in range(50):
        n = n + int(str(n)[::-1])
        if Palindrome(n):
            return False
    return True
        
LychrelNumbers = []
  
for x in range(10000):
    if Lychrel(x):
        LychrelNumbers.append(x)
    
ans = len(LychrelNumbers)