#! python3
# A Tic Tac Toe game which can be played against an IA

import random

# Functions

def print_board(fboard):
    # This function prints the board
    print(fboard[7] + '|' + fboard[8] + '|' + fboard[9])
    print('-+-+-')
    print(fboard[4] + '|' + fboard[5] + '|' + fboard[6])
    print('-+-+-')
    print(fboard[1] + '|' + fboard[2] + '|' + fboard[3])

def check_input(in_val, fboard):
    # This function checks is the box chosen is empty
    try:
        if fboard[int(in_val)] == ' ':
            value = True
        else:
            value = False
    except (ValueError, IndexError):
        value = False
    return value

def check_win(fboard):
    # This funcion checks win conditions are met
    if ((fboard[7]==fboard[8] and fboard[7]==fboard[9] and fboard[7]!=' ') or # Top row
        (fboard[4]==fboard[5] and fboard[4]==fboard[6] and fboard[4]!=' ') or # Mid row
        (fboard[1]==fboard[2] and fboard[1]==fboard[3] and fboard[1]!=' ') or # Low row
        (fboard[7]==fboard[4] and fboard[7]==fboard[1] and fboard[7]!=' ') or # Left col
        (fboard[8]==fboard[5] and fboard[8]==fboard[2] and fboard[8]!=' ') or # Mid col
        (fboard[9]==fboard[6] and fboard[9]==fboard[3] and fboard[9]!=' ') or # Right col
        (fboard[7]==fboard[5] and fboard[7]==fboard[3] and fboard[7]!=' ') or # Diag 7-3
        (fboard[9]==fboard[5] and fboard[9]==fboard[1] and fboard[9]!=' ')    # Diag 9-1
        ):
        value = True
    else:
        value = False
    return value

def ia_check_win(symbol, fboard):
    value = 0
    for i in range(1,10):
        empty = check_input(str(i), fboard)
        if empty == True:
            fboard[i] = symbol
            fwin = check_win(fboard)
            fboard[i] = ' '
            if fwin == True:
                value = i
                break
    return value

def place_random(values, fboard):
    value = 0
    for i in range(4):
        index = random.randint(0,3-i)
        empty = check_input(str(values[index]), fboard)
        if empty == True:
            value = values[index]
            break
        else:
            del values[index]
    return value
    
def ia_best_option(fboard):
    value = 0
    # First comprobation: center
    empty = check_input('5', fboard)
    if empty == True:
        value = 5
    else:
        # Check corners
        value = place_random([1,3,7,9], fboard)
        if value == 0:
            # Check sides
            value = place_random([2,4,6,8], fboard)
    return value
        

# Main -----------------------------------------------------------------------

# Create the board and show its distribution
board = []
for i in range(10):
    board = board + [str(i)]
print('The board is distributed the following way:')
print_board(board)

stop = False
while stop == False:
    # Player configuration
    player = [0]
    while player[0] == 0:
        print('Player 1 chooses X or O')
        sel_aux = input()
        if sel_aux.lower() == 'x':
            player = ['O', 'X']
        elif sel_aux .lower() == 'o':
            player = ['X', 'O']
    while sel_aux.lower() != 'y' and sel_aux.lower ()!= 'n':
        print('Is there a second player?: (Y/N)')
        print('(if not, an IA will play instead)')
        sel_aux = input()
    if sel_aux.lower() == 'y':
        p2 = False
    else:
        p2 = True
    inv_turn = (random.randint(0,1))%2
    if inv_turn == True:
        player.reverse()

    # Clear board
    for i in range(10):
        board[i] = ' '

    # Start game
    win = False
    valid = False
    turn = 0
    while win == False:
        turn += 1
        print('It\'s player ' + str(((turn+inv_turn+1)%2)+1) + ' turn.')
        print('This is the current state of the board.')
        print_board(board)
        # Manage turn
        if (
            (((turn%2) == True and inv_turn == True) or
            ((turn%2) == False and inv_turn == False)) and
            p2 == True
            ): # IA's (Player 2) turn
            box = 0
            box = ia_check_win(player[turn%2],board)            # Check if IA can win
            if box == 0:
                box = ia_check_win(player[(turn%2)-1],board)    # Check if IA can lose
                if box == 0:
                    box = ia_best_option(board)
            else:
                win = True
            board[box] = player[turn%2]
        else:
            while valid == False:
                print('Chose where you want to play.')
                box = input()
                valid = check_input(box,board)
            valid = False
            board[int(box)] = player[turn%2]
            win = check_win(board)
        if turn == 9:
            break
    if win == True:
        print('Player ' + str(((turn+inv_turn+1)%2)+1) + ' has won!')
    else:
        print('Game is over. It\'s a draw.')
    print_board(board)
    
    sel_aux = ' '
    while sel_aux.lower() != 'y' and sel_aux.lower() != 'n':
        print('Do you want to play again? (Y/N)')
        sel_aux = input()
        if sel_aux.lower() == 'y':
            stop = False
        else:
            stop = True

