rows = 12  # Switching rows and columns gives same answer, it is quicker to keep rows bigger
columns = 9
n_blocks = rows * columns // 3  # Number of blocks we need in total

blocks = {(1,columns), (1,columns+1), (columns,columns+1), (columns-1, columns), (columns, 2*columns), (1,2)}  # Postition of two other squares if frst square is at 0
blocks_first_column = {(1,columns), (1,columns+1), (columns,columns+1), (columns, 2*columns), (1,2)}
blocks_second_to_last_column = {(1,columns), (1,columns+1), (columns,columns+1), (columns-1, columns), (columns, 2*columns)}
blocks_last_column = {(columns-1, columns), (columns, 2*columns)}
blocks_second_to_last_row = {(1,columns), (1,columns+1), (columns,columns+1), (columns-1, columns), (1,2)}
blocks_last_row = {(1,2)}

start = {0:1}

def first_zero_position(n):
    pos = 0
    while n & 1:  # While the last bit is 1
        n >>= 1   # Right shift by 1
        pos += 1
    return pos

for _ in range(n_blocks):
    new = {}
    for configuration, possibilities in start.items():
        position = first_zero_position(configuration)
        configuration |= (1<<position)

        if position%columns == 0: # I am in the first column
            possible_blocks = blocks_first_column
        elif position%columns == (columns-1): # I am in the last column
            possible_blocks = blocks_last_column
        elif position%columns == (columns-2):
            possible_blocks = blocks_second_to_last_column
        else:
            possible_blocks = blocks

        if position >= (rows-1) * columns: # I am in the last row
            possible_blocks = possible_blocks.intersection(blocks_last_row)
        elif position >= (rows-2) * columns:
            possible_blocks = possible_blocks.intersection(blocks_second_to_last_row)
        
        for block in possible_blocks:
            possible = True
            new_configuration = configuration
            for pos in block:
                new_pos = position + pos
                if (new_configuration & (1 << new_pos)) == 0:
                    new_configuration |= (1<< new_pos)
                else:
                    possible = False  # If the square is occupied, this block cannot be place
                    break
            if possible:
                if new_configuration in new:
                    new[new_configuration] += possibilities
                else:
                    new[new_configuration] = possibilities

    start = new

print(start[2**(rows*columns)-1])
