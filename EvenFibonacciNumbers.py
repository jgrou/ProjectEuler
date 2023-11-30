ans = 0
F_old = 1
F_new = 1

while F_new <= 4000000:
    F = F_new
    F_new = F_old + F_new
    F_old = F
    if F_new%2==0:
        ans += F_new