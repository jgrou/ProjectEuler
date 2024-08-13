#  0
# 1 2
#  3
# 4 5
#  6
numbers = {}
numbers[0] = {0,1,2,4,5,6}
numbers[1] = {2,5}
numbers[2] = {0,2,3,4,6}
numbers[3] = {0,2,3,5,6}
numbers[4] = {1,2,3,5}
numbers[5] = {0,1,3,5,6}
numbers[6] = {0,1,3,4,5,6}
numbers[7] = {0,1,2,5}
numbers[8] = {0,1,2,3,4,5,6}
numbers[9] = {0,1,2,3,5,6}

transitions = {} # Dictionaries with energy difference for 1 position
for n in numbers:
    for m in numbers:
        transitions[str(n)+str(m)] = 2 * len(numbers[n].intersection(numbers[m]))
        
def PowerDifference(n, m):
    res = 0
    
    for i in range(1,len(m)+1):
        res += transitions[n[-i] + m[-i]]
  
    return res

def DigitalRoot(n):
    res = 0
    for digit in n:
        res += int(digit)
    return str(res)

def Difference(n):
    res = 0
    while len(n) > 1:
        new_number = DigitalRoot(n)
        res += PowerDifference(n, new_number)
        n = new_number
    return res

limit = 2 * 10**7
ans = 0
IsPrime = (limit + 1) * [True]

for p in range(2, int(limit**0.5) + 1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
            
for p in range(10**7 + 1, limit+1, 2):
    if IsPrime[p]:
        ans += Difference(str(p))

print(ans)