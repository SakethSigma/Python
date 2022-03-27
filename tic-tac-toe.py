'''
2 Player Tic-Tac-Toe Game that can be player from the same computer.
'''


def display_board(board):
    '''
    Clears the board and shows the current board status.
    '''
    print("\n"*100)
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print('------------------')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print('------------------')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")

def player_input():
    '''
    Asks Player 1 to select their marker either X or O.
    Rejects invalid input
    '''
    marker = 'a'
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1 pick your marker (X or O): ').upper()
    
    if(marker == 'X'):
        return ['X','O']
    else:
        return ['O','X']

def place_marker(board, marker, position):
    '''
    Places the marker on selected location.
    '''
    board[position] = marker
    
    
    return board

def win_check(board, mark):
    '''
    Checks for win condition after each move.
    '''
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # 1st row
            (board[4] == mark and board[5] == mark and board[6] == mark) or # 2nd row
            (board[7] == mark and board[8] == mark and board[9] == mark) or # 3rd line
            (board[1] == mark and board[4] == mark and board[7] == mark) or # 1st column
            (board[2] == mark and board[5] == mark and board[8] == mark) or # 2nd column
            (board[3] == mark and board[6] == mark and board[9] == mark) or # 3rd column
            (board[1] == mark and board[5] == mark and board[9] == mark) or # 1st diagnal
            (board[3] == mark and board[5] == mark and board[7] == mark)) # 2nd diagn
    

import random

def choose_first():
    '''
    Randomly chooses which player goes first.
    '''
    turn = random.randint(1,2)
    
    print(f'Player {turn} goes first')
    return turn
    

def space_check(board, position):
    '''
    Checks whether the given position has available slot.
    '''
    return board[position] == ' '

def full_board_check(board):
    '''
    Checks if the board is full.
    '''
    return board.count(' ') == 0

def player_choice(board):
    '''
    Asks the player to input their choice on the board and validates the response.

    '''
    inp = False
    game_status = 'on'
    while inp is False:
        pos = input("Enter the position (1-9) for your mark. E for exit ")
        if pos.upper() == 'E':
            game_status = 'off'
            return game_status,0
        
        elif pos.isdigit() == True and (int(pos) in range(1,10)) and space_check(board,int(pos)):
            inp = True
            return game_status,int(pos)
        else:
            print('Please enter a valid position.')
    
    
def replay():
    '''
    Asks if the player wants to play the game again.
    '''
    play_again = input('Play again blyat? R to replay ').upper()
    return play_again == 'R'

'''
Main game
'''
#Welcome Statement
print('Welcome to Tic Tac Toe!')
print('This is a 2 player Tic-Tac-Toe Game')

while True:
    #Set up board list
    board = ['#']+[' ']*9

    #Display board
    #display_board(board)


    #Set random turn
    turn = choose_first();


    #Explain marker. Returns list [player1marker,player2marker]
    markers = player_input(); 


    ready_check = input('Continue? Press Y to continue: ').upper()
    if ready_check == 'Y':
        game_status = 'on'
    else:
        game_status = 'off'




    #While game is on
    while game_status != 'off':

        #If player 1 turn
        if turn == 1:
            #Display Board
            display_board(board)
            #Ask for cell selection
            print('\nPlayer 1 Move\n')
            game_status, position = player_choice(board) #Asks for position. Checks if valid position or asks again. Returns the position

            if game_status == 'off':
                break


            #Mark the position on board
            board = place_marker(board, markers[0], position) #Marks position on board. Display board. Return board



            #check if win
            if win_check(board, markers[0]) == True: #Return True or False indicating game is won or lost.
                #Give message
                display_board(board)
                print('Player 1 wins the game!')
                #Display board

                #End game
                game_status = 'off'

            #Else check if board full
            elif full_board_check(board) == True: #Return True or False indicating board is full or not
                #Give message
                display_board(board)
                print('The game is a draw!')
                #End game
                game_status = 'off'


            #Else switch turn
            else:
                turn = 2

        #If player 2 turn
        if turn == 2:
            #Display Board
            display_board(board)
            #Ask for cell selection
            print('\nPlayer 2 Move\n')
            game_status, position = player_choice(board) #Asks for position. Checks if valid position or asks again. Returns the position

            if game_status == 'off':
                break

            #Mark the position on board
            board = place_marker(board, markers[1], position) #Marks position on board. Display board. Return board
            #Display board
            #display_board(board)

            #check if win
            if win_check(board, markers[1]) == True: #Return True or False indicating game is won or lost.
                #Give message
                display_board(board)
                print('Player 2 wins the game!')
                #Display board

                #End game
                game_status = 'off'


            #Else check if board full
            elif full_board_check(board) == True: #Return True or False indicating board is full or not
                #Give message
                display_board(board)
                print('The game is a draw!')
                #End game
                game_status = 'off'


            #Else switch turn
            else:
                turn = 1   

    if not replay():
        break
    
   

    