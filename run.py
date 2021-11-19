#set variables
playerLetter = 'x'
computerLetter = 'o'

board = [' ' for i in range(10)]
def who_plays_first():
    if random.randint(0, 1) == 0:
        return playerLetter
        else:
            computerLetter
#print the board
def print_board():
    print('***************')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('---------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('---------')
    print(board[7] + '|' + board[8] + '|' + board[9])
print_board()

# checking if the board is full 
def is_full():
    return ' ' not in board[1:10]
   
# check winner
def check_winner(board, letter):
    return (board[1] == board[2] == board[3] == letter) or \
           (board[4] == board[5] == board[6] == letter) or \
           (board[7] == board[8] == board[9] == letter) or \
           (board[1] == board[4] == board[7] == letter) or \
            (board[2] == board[5] == board[8] == letter) or \
            (board[3] == board[6] == board[9] == letter) or \
            (board[1] == board[5] == board[9] == letter) or \
            (board[3] == board[5] == board[7] == letter)
            
        
        # check free space
       def is_space(board, position):
       return board[position] == ' '    

     # place marker on the board 
     def place_marker(board, mark, position):
     board[position] = mark

     #player turn 
     def player_turn():
         position = int(input('choose a position: '))
         try:
             if is_free(board, position):
                 place_marker(board, playerLetter, position)
                 else:
                     print('This position is not free')
                     player_turn()
                     except:
                         if position < 1 or position > 9:
                             print('please choose a number between 1 to 9')
                             player_turn()

                def duplicate_board(board):
                    duplicate_board = []
                    for i in board:
                        duplicate_board.append(i)
                        return duplicate_board
                #computer turn
                def computer_turn():
                    #check if computer wins
                    for i in range(1,10)
                    copy = duplicate_board(board)
                    if is_free(copy, i):
                        place_marker(copy, computerLetter, i)
                        if check_winner(copy, computerLetter):
                            place_marker(board, computerLetter, i)
                            else:
                                continue
                    #check if player wins
                    for i in range(1,10)
                    if is_free(copy, i):
                        place_marker(copy, playerLetter, i)
                        if check_winner(copy, playerLetter):
                            place_marker(board, playerLetter, i)
                            else:
                                continue
                     #run the game
                def main():
                    print('Welcome to the most fun game')
                    turn = who_plays_first()
                    while True:
                        if turn == playerLetter:
                            print_board()
                            player_turn()
                            if check_winner(board, playerLetter):
                                print_board()
                                print('You Won')
                                break
                            elif is_full():
                               
                                print_board()
                                print('Draw!')
                                break
                            else:
                                turn = computerLetter
                                else:
                                    computer_turn()
                                    if check_winner(board, computerLetter):
                                        print_board()
                                        print('You lost!')
                                        break
                                    elif is_full():
                                        print_board()
                                        print('Draw!')
                                        break
                                    else:
                                        turn = playerLetter
                                        main()
                    







