A = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
F = [0,1,1]
ans = 0

for n in range(18):
    limit = (127 + 19 * n) * 7**n
    nth_word = limit // len(A) + 1  # We need this word
    nth_letter = limit % len(A) - 1
    
    while len(A) * F[-1] < limit:
        F.append(F[-1] + F[-2])

    # Now check if nth_word is A or B
    i = len(F) - 1
    while i > 2:
        if nth_word > F[i-2]:
            nth_word -= F[i-2]
            i -= 1
        else:
            i -= 2

    if i == 1:  # nth_word is A
        ans += 10**n * int(A[nth_letter])
    elif i == 2:
        ans += 10**n * int(B[nth_letter])
    else:
        print('error')

print(ans)
