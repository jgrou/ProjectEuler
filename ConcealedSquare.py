def Check(number):
    string = str(number)
    if string[16] != '9':
        return False
    if string[14] != '8':
        return False
    if string[12] != '7':
        return False
    if string[10] != '6':
        return False
    if string[8] != '5':
        return False
    if string[6] != '4':
        return False
    if string[4] != '3':
        return False
    if string[2] != '2':
        return False
    if string[0] != '1':
        return False
    return True

n = int(1020304050607080900**0.5) # Minimum value

while not Check(n**2):
    n += 10 # Last digit of n**2 can only be 0, if last digit of n is 0