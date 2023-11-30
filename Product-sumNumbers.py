N = 12000

minK = N * [99999999] # initialize high default value of min k

def valid(n,k):
    if k >= N: # too many terms
        return False
    if minK[int(k)] > n: # found a smaller number with the same number of terms
        minK[int(k)] = n
        return True
    return False
    
def getMinK(n, product, Sum, depth=1, minFactor=2):
    if product == 1:
        return valid(n, depth+Sum-1)
    result = 0
    if depth > 1:
        if product == Sum: # perfect match
            return valid(n, depth)
        if valid(n, depth + Sum - product):
            result += 1
    
    for i in range(minFactor, int(product**0.5) + 1):
        if product % i == 0:
            result += getMinK(n, product / i, Sum - i, depth + 1, i)
            
    return result

todo = N - 1
n = 4
ans = 0

while todo > 1:
    found = getMinK(n,n,n)
    if found > 0:
        todo -= found
        ans += n
    n += 1