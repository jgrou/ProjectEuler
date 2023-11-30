def PossibleDigits(sudoku, i, j):
    lst = []
    start_row_box = 3 * (i // 3)
    start_column_box = 3 * (j // 3)
    for k in range(9):
        lst.append(sudoku[i][k])
        lst.append(sudoku[k][j])
    for k in range(3):
        for l in range(3):
            lst.append(sudoku[start_row_box + k][start_column_box + l])
    return [x for x in range(1,10) if x not in lst]

def Solver(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for x in PossibleDigits(sudoku, i, j):
                    sudoku[i][j] = x
                    if Solver(sudoku):
                        return True
                    sudoku[i][j] = 0
                return False
    return True

ans = 0

with open('sudoku.txt') as f:
    for line in f:
        line = line.strip()
        if 'Grid' in line: # start of a new puzzle
            puzzle = []  # Initialize a list to store the data for each set
            i = 0
        else:
            numbers = [int(num) for num in line]
            puzzle.append(numbers)
            i += 1
            if i == 9: # After nine rows we have a complete sudoku            
                if Solver(puzzle):
                    string = ''
                    for digit in puzzle[0][:3]:
                        string += str(digit)
                    ans += int(string)