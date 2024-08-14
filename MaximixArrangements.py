limit = 11

# Start with correct arrangement and reverse
# Front -> back -> middlde
result = []

def turn(arrangement, carriage, pos):
    if carriage == -1:
        result.append(arrangement)
        return
    
    if pos == 'front': # Move carriage to the back
        new_arrangement = arrangement[:carriage] + arrangement[carriage:][::-1]
        turn(new_arrangement, carriage, 'back')
        
    elif pos == 'back': # Move carriage to the middle and continue with next carriage in the front
        for i in range(carriage+1, limit-1):
            new_arrangement = arrangement[:i] + arrangement[i:][::-1]
            turn(new_arrangement, carriage-1, 'front')
  
# Beginning is always the same
carriages = res = ''.join(chr(ord('A')+i) for i in range(limit)) 
carriages = carriages[:limit-2] + carriages[limit-2:][::-1] # Switch last one to middle
carriages = carriages[:limit-3] + carriages[limit-3:][::-1] # Switch second to last to back
carriages = carriages[:limit-2] + carriages[limit-2:][::-1] # Switch last one to middle

turn(carriages, limit-4, 'front')
result.sort()
print(result[2010])