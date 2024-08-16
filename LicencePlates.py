# If he sees 0: same number of possiblities
# If he sees 500: he needs another 500
# If he sees antoher number, he needs the opposite of that: 1/1000 numbers

def Win(turn, p, possible_wins, seen, n_total, n0, n500):
    if turn*p < 1e-7:
        return
    
    # See 000
    new_p = p * n0 / n_total
    Win(turn+1, new_p, possible_wins, seen, n_total-1, n0-1, n500)
    
    # See 500
    new_p = p * n500 / n_total
    if n500 < 26**3: # We won
        if turn in P:
            P[turn] += new_p
        else:
            P[turn] = new_p
    else:
        Win(turn+1, new_p, possible_wins, seen, n_total-1, n0, n500-1)
        
    # See something that does not make us win and we did not see
    new_p = p * (n_total - n0 -n500 - seen - possible_wins) / n_total
    Win(turn+1, new_p, possible_wins+26**3, seen+26**3-1, n_total-1, n0, n500)
    
    # See something that we already saw
    new_p = p * seen/n_total
    Win(turn+1, new_p, possible_wins, seen-1, n_total-1, n0, n500)
    
    # See something that makes us win
    new_p = p * possible_wins/n_total
    if turn in P:
        P[turn] += new_p
    else:
        P[turn] = new_p
 
P = {} # P[n] is the probability that we win after n turns
Win(1, 1, 0, 0, n_total=260**3, n0=26**3, n500=26**3)
ans = 0

for key,value in P.items():
    ans += key*value
    
print(round(ans,8))