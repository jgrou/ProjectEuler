# If he sees 0 or something that he has seen before: same number of possiblities
# If he sees 500: he wins if he has seen 500 already
# If he sees antoher number, he needs the opposite of that: 1/1000 numbers

have500 = 500 * [None] # Expected number to win if has seen n plates & plate 500 already
no500   = 500 * [None] # Expected number to win if has seen n cars, but not 500

have500[499] = 2
no500[499]   = 2 * (1 + 1/1000 * have500[499])

for n in range(498, -1, -1):
    p_new  = (998-2*n)/1000 # Probability he sees a car he has not seen before and does not make him win
    p_seen = (n+1)/1000     # Probability he sees a car he has already seen or with plate number 0
    have500[n] = (1 + p_new * have500[n+1]) / (1 - p_seen)
    no500[n]   = (1 + p_new * no500[n+1] + 1/1000 * have500[n]) / (1 - p_seen)
    
print(round(no500[0],8))