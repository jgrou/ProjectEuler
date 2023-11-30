n = 100
List = []

for a in range(2,n+1):
    for b in range(2,n+1):
        power = a**b
        if power not in List:
            List.append(power)

ans = len(List)