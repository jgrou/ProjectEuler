def SumOfConsecutiveSquares(n):
    k = int(n**0.5)
    
    if k**2 == n:
        return False # Exclude squares
    
    while True:
        s = k**2
        i = k
        while s <= n:
            i -= 1
            s += i**2
            
            if s == n:
                return True
            if i <= 1:
                return False
        k -= 1

ans = 0

for i in range(1, 10**4):
    palindrome1 = str(i)[:-1]
    palindrome2 = str(i)
    for digit in str(i)[::-1]:
        palindrome1 += str(digit)
        palindrome2 += str(digit)
    palindrome1, palindrome2 = int(palindrome1), int(palindrome2)
    if SumOfConsecutiveSquares(palindrome1):
        ans += palindrome1
    if SumOfConsecutiveSquares(palindrome2):
        ans += palindrome2
        
#%% Faster
lim=10**8
found=set()

for start in range(1,int(lim**0.5)):
    sos = start*start
    for i in range(start+1,int(lim**0.5)):
        sos += (i*i)
        if sos >= lim: 
            break
        s=str(int(sos))
        if s==s[::-1]:
            found.add(sos)

ans = sum(found)