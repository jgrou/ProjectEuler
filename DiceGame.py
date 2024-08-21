Peter = {}
Colin = {}

def Pyramid(s, turn):
    if turn == 9:
        if s in Peter:
            Peter[s] += 1
        else:
            Peter[s] = 1
        return
    for i in range(1,5):
        Pyramid(s+i, turn+1)
        
def Cube(s, turn):
    if turn == 6:
        if s in Colin:
            Colin[s] += 1
        else:
            Colin[s] = 1
        return
    for i in range(1,7):
        Cube(s+i, turn+1)
    
Pyramid(0,0)
Cube(0,0)
ans = 0

for p in Peter:
    for c in Colin:
        if p > c:
            ans += Peter[p] * Colin[c]
            
ans /= (4**9 * 6**6)
print(round(ans,7))