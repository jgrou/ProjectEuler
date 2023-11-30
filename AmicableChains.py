M = 1_000_000
div = [0]*M
for i in range(1, M):
    for j in range(2 * i, M, i):
        div[j] += i
        
chain = [0] * M # chains: -1 = bad, 0 = untested, n = length of chain
chain[0] = -1

for i in range(1,M):
    if chain[i]: 
        continue
    
    seq = [i]
    
    while div[seq[-1]] < M and chain[div[seq[-1]]] == 0 and div[seq[-1]] not in seq:
        seq.append(div[seq[-1]])
        
    if div[seq[-1]] in seq: #hit a loop
        loop = seq.index(div[seq[-1]])
        
        for l in range(loop):
            chain[seq[l]] = -1 #pre-loop: mark as bad
            
        for l in range(loop, len(seq)):
            chain[seq[l]] = len(seq) - loop #within-loop: mark chain length
            
    else: #exceeded lim or hit a bad number
        for s in seq: 
            chain[s] = -1 #mark as bad
    
answer = chain.index(max(chain))