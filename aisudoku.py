def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(board):
    """Find an empty space in the board with the least candidates (MRV heuristic)"""
    empty_list = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                num_possibilities = len(get_possibilities(board, i, j))
                empty_list.append((num_possibilities, i, j))
    if not empty_list:
        return None
    empty_list.sort()  # Sort by number of possibilities
    return empty_list[0][1], empty_list[0][2]  # return position with least possibilities

def get_possibilities(board, row, col):
    """Returns the possible numbers for a given cell"""
    possibilities = set(range(1, 10))
    # Exclude numbers already in the same row, column, and box
    for k in range(9):
        if board[row][k] in possibilities:
            possibilities.remove(board[row][k])
        if board[k][col] in possibilities:
            possibilities.remove(board[k][col])
    box_x, box_y = 3 * (col // 3), 3 * (row // 3)
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] in possibilities:
                possibilities.remove(board[i][j])
    return possibilities

def solve(board):
    """Solves a sudoku board using backtracking with the MRV and LCV heuristics"""
    find = find_empty(board)
    if not find:
        return True  # Solution found
    else:
        row, col = find

    possibilities = get_possibilities(board, row, col)
    for value in sorted(possibilities, key=lambda x: -count_constraints(board, row, col, x)):
        board[row][col] = value
        if solve(board):
            return True
        board[row][col] = 0  # Backtrack

    return False  # Trigger backtracking

def count_constraints(board, row, col, num):
    """Count how many options this choice would eliminate for surrounding cells (LCV heuristic)"""
    count = 0
    for i in range(9):
        if board[row][i] == 0:
            if num in get_possibilities(board, row, i):
                count += 1
        if board[i][col] == 0:
            if num in get_possibilities(board, i, col):
                count += 1
    box_x, box_y = 3 * (col // 3), 3 * (row // 3)
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == 0:
                if num in get_possibilities(board, i, j):
                    count += 1
    return count

if __name__ == "__main__":
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve(sudoku_board):
        print_board(sudoku_board)
    else:
        print("No solution exists")