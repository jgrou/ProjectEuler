sides = 12
dices = 20
top = 10
aim = 70

# Check in how many ways we can roll each possible top 10: sides**top
# Keep keys sorted to reduce number of keys
ways = {top * (0,) :1}

for dice in range(dices):
    new_ways = {}
    for key, value in ways.items():
        for roll in range(1, sides+1):
            if roll > key[-1]:
                new_key = list(key)[:-1] + [roll]
                new_key.sort(reverse=True)
                new_key = tuple(new_key)
            else:
                new_key = key
            if sum(new_key) <= aim:
                if new_key in new_ways:
                    new_ways[new_key] += ways[key]
                else:
                    new_ways[new_key] = ways[key]
    ways = new_ways

# Now compute how many sum up to aim
ans = 0

for key, value in ways.items():
    if sum(key) == aim:
        ans += value
