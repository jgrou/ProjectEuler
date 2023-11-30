CycleLength = 1000 * [0]

for d in range(1,1000):
    residual = 1
    ListOfResiduals = []
    
    while residual not in ListOfResiduals:
        ListOfResiduals.append(residual)
        residual *= 10
        residual = residual -  d * int(residual/d)  
        if residual == 0:
            break

    if residual != 0:
        CycleLength[d] = len(ListOfResiduals) - ListOfResiduals.index(residual)
    
ans = CycleLength.index(max(CycleLength))