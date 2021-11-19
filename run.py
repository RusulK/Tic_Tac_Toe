# set variables
playerLetter = 'x'
computerLetter = 'o'

board = [' ' for i in range(10)]
#print the board
def print_board():
    print('***************')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('---------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('---------')
    print(board[7] + '|' + board[8] + '|' + board[9])
print_board()

