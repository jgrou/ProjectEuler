from collections import Counter

# Lists to store the words
Player1 = []
Player2 = []

with open('poker.txt') as f:
    for line in f:
        words = line.strip().split()  # Splitting the line into words
        Player1.append(words[:5])
        Player2.append(words[5:])
   
names = [str(i) for i in range(2,10)] + ['T', 'J', 'Q', 'K', 'A']
values = dict(zip(names, range(len(names))))

def rank(hand):
    number_values = [values[i[0]] for i in hand]
    number_values.sort(reverse=True)
    counter = Counter(number_values)
    most_common_element, count = counter.most_common(1)[0] # Find most frequent number
    rest = [i for i in number_values if i != most_common_element]
    
    # Straight flush
    if len(set([i[1] for i in hand])) == 1: 
        if count == 1 and max([number_values[j] - number_values[j+1] for j in range(4)]) == 1:
            return 9, [number_values[0]]
        if number_values == [0,1,2,3,12]: # Ace can also count as 1
            return 9, [3]
        
    if count == 4: # Four of a kind
        return 8, [most_common_element, max(rest)]
    elif len(set(number_values)) == 2: # Full house
        return 7, [most_common_element, max(rest)]
    elif len(set([i[1] for i in hand])) == 1: # Flush
        return 6, number_values
    
    # Straight
    elif count == 1 and max([number_values[j] - number_values[j+1] for j in range(4)]) == 1:
        return 5, [number_values[0]]
    elif number_values == [0,1,2,3,12]: # Ace can also count as 1
        return 5, [3]
    
    elif count == 3: # Three of a kind
        return 4, [most_common_element] + rest
    elif len(set(number_values)) == 3: # Two pair
        return 3, [counter.most_common()[0][0], counter.most_common()[1][0], counter.most_common()[2][0]]
    elif len(set(number_values)) == 4: # One pair
        return 2, [most_common_element] + rest
    else:
        return 1, number_values
    
def win(hand1, hand2):
    rank1, value1 = rank(hand1)
    rank2, value2 = rank(hand2)
    
    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return 2
    else:
        for i in range(len(value1)):
            if value1[i] > value2[i]:
                return 1
            if value2[i] > value1[i]:
                return 2
        return 0
 
ans = 0

for i in range(len(Player1)):
    if win(Player1[i], Player2[i]) == 0:
        print('error')
    if win(Player1[i], Player2[i]) == 1:
        ans += 1