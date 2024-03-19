ans = []

def Prime(n):
    for i in range(2, int(n**0.5+1)):
        if n%i == 0:
            return False
    return True

def Permutation(n, k):
    for digit in str(n):
        if digit not in str(k):
            return False
    for digit in str(k):
        if digit not in str(n):
            return False
    return True

for x in range(10**3,10**4):
    if Prime(x):
        for increase in range(1,int((10**4 - x) / 2)):
            if Permutation(x, x+increase):
                if Prime(x+increase):
                    if Permutation(x, x+2*increase):
                        if Prime(x+2*increase):
                            ans.append(str(x)+str(x+increase)+str(x+2*increase))
