digit = [str(i) for i in range(1,8)]
digit.sort(reverse=True)
                                    
def IsPandigital(n):
    if '0' in str(n):
        return False
    for i in range(1,len(str(n))+1):
        if str(i) not in str(n):
            return False
    return True

def IsPrime(x):
    for p in range(2,int(x**0.5+1)):
        if x%p==0:
            return False
    return True

def main():
    for i in reversed(range(7654322)):
        if IsPandigital(i):
            if IsPrime(i):
                return i
                
ans = main()
