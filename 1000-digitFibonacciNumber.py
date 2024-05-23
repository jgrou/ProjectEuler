F_old = 1
F_new = 1
i = 2

while len(str(F_new)) < 1000:
    F_new, F_old = F_old + F_new, F_new
    i+=1