def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row,n), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def print_board(board):
    for row in board:
        print(" ".join(['Q' if x else '.' for x in row]))

# Example usage
n = int(input("Enter value of N for N-Queens: "))
board = [[0]*n for _ in range(n)]
if solve_n_queens(board, 0, n):
    print("Solution:")
    print_board(board)
else:
    print("No solution found.")
