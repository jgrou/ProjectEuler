exponents = {1: [[1]]} # Store all minimum ways to make an exponent as we might need different for higher exponents

while 200 not in exponents:
    keys = list(exponents.keys())
    for key1 in keys:
        for key2 in keys:
            new_key = key1+key2
            
            try:
                new_power_set = exponents[new_key] # Try to access a key that may not exist
                min_len = len(new_power_set[0])
            except KeyError:
                min_len = 1000 # If it does not exist, put ridiculous high min_len
                
            for set1 in exponents[key1]:
                for set2 in exponents[key2]:
                    new_set = list(set(set1).union(set(set2)))
                    new_set.append(new_key)
                    if len(new_set) < min_len:
                        new_power_set = [new_set]
                        min_len = len(new_set)
                    elif len(new_set) == min_len:
                        if new_set not in new_power_set:
                            new_power_set.append(new_set)
            exponents[new_key] = new_power_set

ans = 0
            
for k in range(2,201):
    ans += len(exponents[k][0]) - 1