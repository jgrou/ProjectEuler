den = 2
AF = {2}
lower = 1
c = (5**0.5 - 1) / 2 # Maximal value of x

while len(AF) < 15:
    for num in range(lower+1, int(c*den)+1):
        x = num * den
        y = den**2 - num * den - num**2
        A_F = x // y
        if A_F * y == x:
            AF.add(A_F)
            lower = num # Assume we find them in increasing order
    den += 1