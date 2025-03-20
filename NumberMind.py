import itertools
import random
from copy import deepcopy

guesses = {
'5616185650518293':2,
'3847439647293047':1,
'5855462940810587':3,
'9742855507068353':3,
'4296849643607543':3,
'3174248439465858':1,
'4513559094146117':2,
'7890971548908067':3,
'8157356344118483':1,
'2615250744386899':2,
'8690095851526254':3,
'6375711915077050':1,
'6913859173121360':1,
'6442889055042768':2,
'2321386104303845':0,
'2326509471271448':2,
'5251583379644322':2,
'1748270476758276':3,
'4895722652190306':1,
'3041631117224635':3,
'1841236454324589':3,
'2659862637316867':2}

# All 22 guesses and how many digits were correct
sequences = []
hits = []

for guess, matches in guesses.items():
    s = [int(c) for c in guess]
    sequences.append(s)
    hits.append(matches)
    
num_digits = len(sequences[0])

#%% Brute force
possibilities = [set(range(10)) for _ in range(num_digits)] # Initialize all possible digits for each position
    
def f(possible, guess=0):
    if guess == len(sequences): # Base case: processed all guesses
        print(possible)
        return
    key = sequences[guess]
    value = hits[guess]
    
    for correct in itertools.combinations(range(num_digits), value):
        new_possibilities = deepcopy(possible)
        stop = False
        
        for pos in range(num_digits):
            if pos in correct:
                if key[pos] not in new_possibilities[pos]:
                    stop = True
                    break
                new_possibilities[pos] = {key[pos]}
            else:
                if key[pos] in new_possibilities[pos]:
                    new_possibilities[pos].remove(key[pos])
                if not new_possibilities[pos]:
                    stop = True
                    break                    
        
        if not stop:      
            f(new_possibilities, guess+1)
 
f(possibilities)

#%% Random guessing
# Replace reference by a new random digit (0..9)
def shuffle(digit):
    old = digit
    while True:
        digit = random.randint(0,9)
        if digit != old:
            break
    return digit

# Compute how many digits of the guesses don't match to the currently analyzed number
# A perfect match returns 0, "mismatches" return > 0
def distance(current):
    errors = 0
    for i in range(len(sequences)):
        # Count number of matching digits
        same = sum(1 for j in range(len(current)) if current[j] == sequences[i][j])
        # Too many identical digits?
        if same > hits[i]:
            errors += same - hits[i]
        else: # Or too few?
            errors += hits[i] - same
    return errors

# Initially a purely random guess
current = [random.randint(0,9) for _ in range(num_digits)]

# Shuffle a random digit when stuck in a local optimum
max_rounds_without_improvement = 20
quiet_rounds = 0

errors = distance(current)
previous = errors

while errors != 0:
    # Replace every digit by a different random number, keep those that minimize the error metric
    for i in range(num_digits):
        previous_digit = current[i]
        current[i] = shuffle(previous_digit)

        # Compute error metric
        modified = distance(current)
        if modified <= errors:
            # Better than before, adjust error level and keep new digit
            errors = modified
        else:
            # Mutation is equal or worse, restore old digit
            current[i] = previous_digit
        
    # Unchanged score ? We didn't improve on the previous solution ...
    if errors == previous:
        # Stuck too long? Try to escape local optimum
        quiet_rounds += 1
        if quiet_rounds == max_rounds_without_improvement:
            # Change a random number
            index = random.randint(0,num_digits-1)
            current[index] = shuffle(current[index])
            errors = distance(current)

            # Reset counter
            quiet_rounds = 0
    else:
        # We got closer to the goal...
        quiet_rounds = 0
        previous = errors

# Show solution
print(''.join(map(str, current)))