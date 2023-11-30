n = 1
p = [1]
    
while True:
    temp = 0
    k = 0
    while True:
        k += 1
        j = (k * (3 * k - 1)) // 2
        if (j > n):
            break
        temp += (-1)**(k+1) * p[n - j]
        j = (k * (3 * k + 1)) // 2
        if (j > n):
            break
        temp += (-1)**(k+1) * p[n - j]
    p.append(temp)
    if temp % 10**6 == 0:
        break
    n += 1