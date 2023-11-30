import random

DiceSides = 6

def CommunityChest(i, pos):
    if i == 1:
        return 0
    elif i == 2:
        return 10
    else:
        return pos
    
def Chance(i, pos):
    if i == 1:
        return 0
    elif i == 2:
        return 10
    elif i == 3:
        return 11
    elif i == 4:
        return 24
    elif i == 5:
        return 39
    elif i == 6:
        return 5
    elif i == 7 or i == 8:
        if pos == 36:
            return 5
        elif pos == 7:
            return 15
        elif pos == 22:
            return 25
    elif i == 9:
        if pos == 36 or pos == 7:
            return 12
        elif pos == 22:
            return 28
    elif i == 10:
        return pos - 3
    else:
        return pos

position = 0 # start at go
cc_counter = 1 # first card is on top
ch_counter = 1
double_counter = 0
visit_counter = {i:0 for i in range(40)}

for _ in range(100000):
    dice_roll1 = random.randint(1, DiceSides) 
    dice_roll2 = random.randint(1, DiceSides)
    
    if dice_roll1 == dice_roll2:
        double_counter += 1
    else:
        double_counter = 0
    
    # Throwing double thrice means going to jail
    if double_counter == 3:
        position = 10
        double_counter = 0
    else:
        position += dice_roll1 + dice_roll2
        position = position % 40
        
    # Landing on chance
    if position == 7 or position == 22 or position == 36:
        position = Chance(ch_counter, position)
        ch_counter += 1
        if ch_counter == 17:
            ch_counter = 1
    
    # Landing on community chest
    if position == 2 or position == 17 or position == 33:
        position = CommunityChest(cc_counter, position)
        cc_counter += 1
        if cc_counter == 17:
            cc_counter = 1
        
    # Go to jail
    if position == 30:
        position = 10
        
    visit_counter[position] += 1