# https://oeis.org/A255938
# https://en.wikipedia.org/wiki/Langton's_ant
# After 9976 moves the ant starts building a recurrent "highway" pattern of 104 steps that repeats indefinitely.

limit = 10**18 # limit = 9977 + 104*q + r
q = (limit - 9977)//104
r = (limit - 9977)%104

black = set()  # Set of squares that are black, initially empty

# Start by going right, should not matter
x_direction = 1
y_direction = 0

# Start at (0,0), should not matter
x = 0
y = 0

for move in range(9977+r):
    if (x,y) in black:
        black.remove((x,y)) # Flips the color of the square to white
        x_direction, y_direction = -y_direction, x_direction # Rotates counter clockwise
    else:
        black.add((x,y)) # Flips the color of the square to black
        x_direction, y_direction = y_direction, -x_direction # Rotates clockwise

    # Moves forward one square
    x += x_direction
    y += y_direction

ans = len(black) + 12 * q

