regions = {}
doubles = {}

singles = []
for i in range(1,21):
    regions['S'+str(i)] = i
    regions['D'+str(i)] = 2 * i
    regions['T'+str(i)] = 3 * i
    doubles['D'+str(i)] = 2 * i

# Add bull
regions['S25'] = 25
regions['D25'] = 50
doubles['D25'] = 50

def NumberOfCheckouts(n):
    sol = 0
    for d in doubles:
        rest = n - doubles[d]
        if rest == 0:
            sol += 1
        elif rest > 0:
            for x in regions:
                if regions[x] == rest:
                    sol += 1
                elif regions[x] < rest:
                    new_rest = rest - regions[x]
                    for y in regions:
                        if regions[y] == new_rest:
                            if x == y:
                                sol += 1
                            else:
                                sol += 0.5 # We count these solutions twice
    return sol

ans = 0
                           
for n in range(2,100):
    ans += NumberOfCheckouts(n)