def tic_tac_toe():
    print(f'{" " * 6}{"|" * 3}{" " * 6}{"|" * 3}{" " * 6}')  # top of tic
    print(f' {"|" * 4} {"|" * 3}  {"|" * 2}  {"|" * 3} {"|" * 4}')
    print(f'  {"|" * 2}  {"|" * 3}  {"|" * 2}  {"|" * 3} {"|" * 2}')
    print(f'  {"|" * 2}  {"|" * 3}  {"|" * 2}  {"|" * 3} {"|" * 2}')
    print(f'  {"|" * 2}  {"|" * 3}  {"|" * 2}  {"|" * 3} {"|" * 4}')
    print(f'{" " * 6}{"|" * 3}{" " * 6}{"|" * 3}{" " * 6}')
    print(f'{"=" * 24}')
    print(f'{"=" * 24}')
    print(f'{" " * 6}{"|" * 3}{" " * 6}{"|" * 3}{" " * 6}')  # top of tac
    print(f' {"|" * 4} {"|" * 3}  {"=" * 2}  {"|" * 3} {"|" * 4}')
    print(f'  {"|" * 2}  {"|" * 3} |  | {"|" * 3} {"|" * 2}')
    print(f'  {"|" * 2}  {"|" * 3} |==| {"|" * 3} {"|" * 2}')
    print(f'  {"|" * 2}  {"|" * 3} |  | {"|" * 3} {"|" * 4}')
    print(f'{" " * 6}{"|" * 3}{" " * 6}{"|" * 3}{" " * 6}')
    print(f'{"=" * 24}')
    print(f'{"=" * 24}')
    print(f'{" " * 6}{"|" * 3}{" " * 6}{"|" * 3}{" " * 6}')  # top of toe
    print(f' {"|" * 4} {"|" * 3} .==. {"|" * 3} {"|" * 4}')
    print(f'  {"|" * 2}  {"|" * 3} |  | {"|" * 3} {"|" * 2}__')
    print(f'  {"|" * 2}  {"|" * 3} |  | {"|" * 3} {"|" * 2}￣')
    print(f'  {"|" * 2}  {"|" * 3} \'==\' {"|" * 3} {"|" * 4}')
    print(f'{" " * 6}{"|" * 3}{" " * 6}{"|" * 3}{" " * 6}')

    print('*********Instruction****')
    print('* player needs to choose a position between 0 - 8.')
    print('* player will play against the computer.')
    print('* At the end of the game, who ever wins,')
    print(' would choose to play again or to exist the game.')
    print('* If no one wins and the board run out of space would be Draw!')
    print('* you will be asked to run the game again.')
    print('* **********ENJOY*********')
