def CheckPalindrome(n):
    string = str(n)
    
    for i in range(int(len(string) / 2)):
        if string[i] != string[-(i+1)]:
            return False
    return True
 
DoublePalindromes = []   

for n in range(10**6):
    if CheckPalindrome(n):
        i = 0
        while 2**i <= n:
            i+=1
        
        binary = '1'
        residual = n - 2**(i-1)
        k = i-2
        
        for _ in range(i-1):
            if 2**k <= residual:
                residual -= 2**k
                binary += '1'
            else:
                binary += '0'
            k-=1
        
        if CheckPalindrome(binary):
            DoublePalindromes.append(n)
            
ans = sum(DoublePalindromes)
