players = 100
d = (players//2 + 1) * [0]  # Probability distribution of the distance
d[-1] = 1
ans = 0
turn = 1
delta = 0
epsilon = 1e-11

while delta >= 1e-11 or turn <= players**2:
    new_d = (players//2 + 1) * [0]
    for current in range(1, players//2 + 1):
        minus2 = 1/36
        minus1 = 8/36
        same = 18/36
        plus1 = 8/36
        plus2 = 1/36

        if current == 1:
            same += minus2
            minus2 = 0
        elif current == players//2 - 1:
            same += plus2
            plus2 = 0
        elif current == players//2:
            minus2 += plus2
            minus1 += plus1
            plus2 = 0
            plus1 = 0
            
        if current >= 2:
            new_d[current-2] += minus2 * d[current]
        new_d[current-1] += minus1 * d[current]
        new_d[current] += same * d[current]
        if current < players//2:
            new_d[current+1] += plus1 * d[current]
        if current < players//2 - 1:
            new_d[current+2] += plus2 * d[current]

    d = new_d
    delta = d[0] * turn
    ans += delta
    turn += 1

print(round(ans,6))
