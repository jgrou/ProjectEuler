# nim-sum binary digital sum calculated using bitwise xor
# The winning strategy is to finish every move with a nim-sum of 0. 
# This is always possible if the nim-sum is not zero before the move
# If the nim-sum is zero, then the next player will lose if the other player does not make a mistake
# numbers whose binary representation contains no two adjacent 1's.

ans = 0
max_length = 30

def recursive(current_length, previous_bit):
    if current_length == max_length:
        yield 1
        return
    
    yield from recursive(current_length+1, 0)
    
    if previous_bit == 0:
        yield from recursive(current_length+1, 1)
        
for _ in recursive(0, 0):
    ans += 1