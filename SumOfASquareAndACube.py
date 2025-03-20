limit = 1000000000  # This limit happens to find 5
square_limit = int(limit**0.5)
PalindromicNumbers = {}

def IsPalindrome(n):
    x = str(n)
    for i in range(len(x)//2):
        if x[i] != x[-(i+1)]:
            return False
    return True

for square in range(1,square_limit+1):
    cube_limit = int((limit - square**2)**(1/3))
    for cube in range(1, cube_limit+1):
        n = square**2 + cube**3
        if IsPalindrome(n):
            if n in PalindromicNumbers:
                PalindromicNumbers[n] += 1
            else:
                PalindromicNumbers[n] = 1
                
ans = sum([key for key in PalindromicNumbers.keys() if PalindromicNumbers[key] == 4])
