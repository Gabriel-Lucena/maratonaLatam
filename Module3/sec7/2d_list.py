board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)

board = [["EMPTY" for i in range(8)] for j in range(8)]

board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"

board[4][2] = "KNIGHT"

board[3][4] = "PAWN"

print(board)
