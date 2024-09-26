limit = 10**9

# Huffman_coding, but keep track of how many strings with certain costs there are
costs = 68 * [0] # Empirically the length necessary
costs[1] = 1
costs[4] = 1
x = 1
remaining = limit-2
ans = 5

while remaining > 0:
    block = costs[x]

    if block > remaining:
        block = remaining
        
    costs[x+1] += block
    costs[x+4] += block
    remaining -= block
    costs[x] -= block
    ans += block * (x+5)
    x += 1
    
print(ans)