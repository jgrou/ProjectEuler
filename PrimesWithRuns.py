def IsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5), 2):
        if n%i == 0:
            return False
    return True

N = 10

def Replace(ListOfstring, d):
    lst = []
    
    for string in ListOfstring:
        for other_digit in range(10):
            if other_digit != d:
                for i in range(N):
                    if string[i] != str(other_digit): # Do not replace with itself
                        new_string = string[:i] + str(other_digit) + string[i+1:]
                        lst.append(new_string)
    return lst
                
def solutions(d, M):
    S = 0
    string = N * str(d)
    ListOfString = [string]
    
    for _ in range(N - M): # N-M digits are not d
        ListOfString = Replace(ListOfString, d)
    
    for string in ListOfString:
        if IsPrime(int(string)) and string[0] != str(0):
            S += int(string)
    return S
        
def Main(d):
    S = 0
    M = N
    
    while S == 0:
        M -= 1
        S = solutions(d , M)
    
    return M, S

ans = 0

for i in range(10):
    M, S = Main(i)
    if M == N - 2:
        ans += S//2
    elif M == N-1:
        ans += S
    else:
        print('Help')