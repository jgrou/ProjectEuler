target = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'           
a1 = -1
Found = False

while not Found: 
    a1 += 2 # Because the last step is 'd', the final value should be odd
    a = a1
    for index, step in enumerate(target[::-1]):
        if step == 'D':
            a *= 3
        elif step =='U':
            a = 3 * a - 2
            if a%4 == 0:
                a //= 4
            else:
                index -= 1 # Otherwise it terminates even though the last step is incorrect
                break
        elif step == 'd':
            a = 3 * a + 1
            if not a&1: # even
                a //= 2
            else:
                index -= 1
                break
    if index == len(target) - 1 and a > 10**15:
        Found = True