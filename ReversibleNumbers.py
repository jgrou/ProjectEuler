limit = 10**9
ReversibleNumers = set()

def OddDigits(k):
    for digit in str(k):
        if int(digit)%2 == 0:
            return False
    return True

for n in range(11, limit):
    if str(n)[-1] != '0':
        reverse = int(str(n)[::-1])
        number = n + reverse
        if OddDigits(number):
            ReversibleNumers.add(n)
            ReversibleNumers.add(reverse)