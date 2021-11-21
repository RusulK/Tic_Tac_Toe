from random import randint
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
# # testing
# print_board()
# print(check_winner(board, playerLetter))
# print(check_winner(board, computerLetter))


# check free space
def is_free(board, position):
    return board[position] == ' '


# place marker on the board 
 #def place_marker(board, mark, position):
    #board[position] = mark
#print(place_marker(board, mark, position))


# who plays first
#def who_plays_first():
 #   if random.randint(0,1) == 0:
#        return playerLetter
#    else:
#            return computerLetter
 #print(who_plays_first())
#      #player turn 
# def player_turn():
#     position = int(input('choose a position: '))
#     try:
#         if is_free(board, position):
#             place_marker(board, playerLetter, position)
#         else:
#             print('This position is not free')
#             player_turn()
#     except:
#         if position < 1 or position > 9:
#             print('please choose a number between 1 to 9'



                             
#     #create a copy of the board
# def duplicate_board(board):
#     duplicate_board = []
#     for i in board:
#         duplicate_board.append(i)
#     return duplicate_board
#     #computer turn
# def computer_turn():
#     #check if computer wins
#     for i in range(1,10):
#         copy = duplicate_board(board)
#         if is_free(copy, i):
#             place_marker(copy, computerLetter, i)
#         if check_winner(copy, computerLetter):
#             place_marker(board, computerLetter, i)
#             return
#         else:
#             continue
# #check if player wins
# for i in range(1,10)
# if is_free(copy, i):
#     place_marker(copy, playerLetter, i)
# if check_winner(copy, playerLetter):
#     place_marker(board, computerLetter, i)
# return
# else:
# continue
# #run the game
# def main():
# print('Welcome to the most fun game')
# turn = who_plays_first()
# while True:
# if turn == playerLetter:
# print_board()
# player_turn()
# if check_winner(board, playerLetter):
# print_board()
# print('You Won')
# break
# elif is_full():

# print_board()
# print('Draw!')
# break
# else:
# turn = computerLetter
# else:
# computer_turn()
# if check_winner(board, computerLetter):
# print_board()
# print('You lost!')
# break
# elif is_full():
# print_board()
# print('Draw!')
# break
# else:
# turn = playerLetter
# main()
