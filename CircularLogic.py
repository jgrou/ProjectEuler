limit = 6
new_bit = (2**limit) * [None]

for bit1 in range(2**limit):
    a = bit1 // 2**(limit-1)
    bit2 = bit1 - a * 2**(limit-1)
    b = bit2 // 2**(limit-2)
    bit3 = bit2 - b * 2**(limit-2)
    c = bit3 // 2**(limit-3)
    new_bit[bit1] = 2 * bit2 + a ^(b and c)

# We see some cyclic maps, which cannot have two 1's next to each other
cycles = []
seen = set()

for k in range(2**limit):
    if k in seen:
        continue
    cycle = set()
    x = k
    while new_bit[x] not in cycle:
        x = new_bit[x]
        seen.add(x)
        cycle.add(x)
    cycles.append(cycle)

cycle_lengths = [len(cycle) for cycle in cycles]

# Lucas numbers
L = [2,1]

for cycle_length in range(2, max(cycle_lengths)+1):
    L.append(L[-1] + L[-2])
    
ans = 1
for cycle_length in cycle_lengths:
    ans *= L[cycle_length]
