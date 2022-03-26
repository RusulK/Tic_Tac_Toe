from random import randint
import intro

intro.tic_tac_toe()
# set variables
playerLetter = '  x  '
computerLetter = '  o  '


# print the board
def print_board(board):
    print('*' * 17)
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-' * 17)
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-' * 17)
    print(board[6] + '|' + board[7] + '|' + board[8])


# checking if the board is full
def is_full(board):
    return '     ' not in board[:9]


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
    return board[position] == '     '


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
def player_turn(board):
    position_input = input('please choose a position(0-8): ')
    try:
        if position_input.isnumeric():
            position = int(position_input)
        else:
            raise ValueError(
                f'{position_input} is not a number, '
                'please choose a number between 0 - 8: '
                )
        if position < 0 or position > 8:
            raise ValueError('Please choose a number between 0 - 8: ')
        if is_free(board, position):
            place_marker(board, playerLetter, position)
        else:
            print('This position is not free')
            player_turn(board)
    except ValueError as e:
        print(e)
        player_turn(board)


# computer turn
def computer_turn(board):
    position = randint(0, 8)
    if is_free(board, position):
        place_marker(board, computerLetter, position)
    else:
        computer_turn(board)


# switch player and computer
current_player = who_plays_first()


def switch_player():
    global current_player
    if current_player == playerLetter:
        current_player = computerLetter
    else:
        current_player = playerLetter


# Current Player
def current_player_turn(board):
    if current_player == playerLetter:
        player_turn(board)
    else:
        computer_turn(board)


# run the game
def main():
    board = ['     ' for i in range(9)]
    print('Welcome to Tic Tac Toe (❁´◡`❁)')
    play = input("Do you want to play? (yes/no) ")
    if play.lower() == "yes":
        print("cool..let's play :)")
    elif play.lower() == "no":
        print('sorry to see you go :(')
        quit()
    else:
        print('please choose yes/no to start or quit the game')
        main()

    replay = True
    while replay:
        print_board(board)
        switch_player()
        current_player_turn(board)
        if check_winner(board, current_player):
            print_board(board)
            print(current_player + 'won')
            play = input('do you want to play again?(yes/no) ')
            if play.lower() == 'yes':
                print("cool... let's play again")
                board = ['     ' for i in range(9)]
            else:
                replay = False
                print('sorry to see you go :(')
        elif is_full(board):
            print_board(board)
            print('Draw!')
            play = input('do you want to play again? ')
            if play.lower() == 'yes':
                print("cool... let's play again")
                board = ['     ' for i in range(9)]
            else:
                replay = False
                print('sorry to see you go :(')


main()
