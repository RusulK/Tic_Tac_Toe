from random import randint
import intro

intro.tic_tac_toe()
# set variables
playerLetter = 'x'
computerLetter = 'o'

board = [' ' for i in range(9)]
# testing
# board[0] = playerLetter
# board[4] = playerLetter
# board[8] = playerLetter
# board[0] = computerLetter
# board[1] = computerLetter
# board[2] = computerLetter


# print the board
def print_board():
    print('***************')
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('---------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('---------')
    print(board[6] + '|' + board[7] + '|' + board[8])


# checking if the board is full
def is_full():
    return ' ' not in board[:9]


# check winner
def check_winner(board, letter):
    return (board[0] == board[1] == board[2] == letter) or \
           (board[3] == board[4] == board[5] == letter) or \
           (board[6] == board[7] == board[8] == letter) or \
           (board[0] == board[3] == board[6] == letter) or \
           (board[1] == board[4] == board[7] == letter) or \
           (board[2] == board[5] == board[8] == letter) or \
           (board[0] == board[4] == board[8] == letter) or \
           (board[2] == board[4] == board[6] == letter)


# check free space
def is_free(board, position):
    return board[position] == ' '


# place marker on the board
def place_marker(board, mark, position):
    board[position] = mark


# who plays first
def who_plays_first():
    if randint(0, 1) == 0:
        return playerLetter
    else:
        return computerLetter
# print(who_plays_first())
# print_board()


# player turn
def player_turn():
    position = int(input('please choose a number between 0 - 8: '))
    if is_free(board, position):
        place_marker(board, playerLetter, position)
    else:
        print('This position is not free')
        player_turn()


# computer turn
def computer_turn():
    position = randint(0, 8)
    if is_free(board, position):
        place_marker(board, computerLetter, position)
    else:
        computer_turn()


# switch player and computer
current_player = who_plays_first()


def switch_player():
    global current_player
    if current_player == playerLetter:
        current_player = computerLetter
    else:
        current_player = playerLetter


# Current Player
def current_player_turn():
    if current_player == playerLetter:
        player_turn()
    else:
        computer_turn()
        

# run the game
def main():
    print('Welcome to Tac Tic Toe :)')
    while True:
        print_board()
        switch_player()
        current_player_turn()
        if check_winner(board, current_player):
            print_board()
            print(current_player + 'won')
            break
        if is_full():
            print_board()
            print('Draw!')
            break


main()
