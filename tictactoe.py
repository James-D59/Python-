import os



#clear the screen
def clear_screen():
    os.system("cls")

'''
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9

'''

# Print the board
def print_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]} ')
    print ('--+---+--')
    print(f'{board[3]} | {board[4]} | {board[5]} ')
    print ('--+---+--')
    print(f'{board[6]} | {board[7]} | {board[8]} ')
    print()

# Check for winner
def check_winner(board, current_player):
    #define winning combinations
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8], #rows
        [0,3,6], [1,4,7], [2,5,8], #columns
        [0,4,8], [2,5,6], #diagonals

    ]

    #check in any winning combination is met
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] ==board[combination [2]] == current_player:
            return True
    return False

#check for a draw
def check_draw(board):
    return all(spot in ["X", "O"] for spot in board)
  
    

# main function
def play_tic_tac_toe():
    #initialize board and empty spots will be represented by numbers
    #['1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = [str(i) for i in range (1,10) ]
    
    #define players
    current_player = "X"

    #main game loop
    while True:
        
        print_board(board)

        #get player move
        move = input(f'Player {current_player}, enter your move (1-9)')

        #validate move
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print('Invalid input please enter a number between 1 and 9')
            input("Press Enter to continue...")
            continue

        #convert move number to index nmber by subtracting 1
        move = int(move) - 1

        #check if spot is already taken
        if board[move] in ['X', 'O']:
            print('That spot is already taken. Try again.')
            input("Press Enter to continue...")
            continue

        clear_screen()
        #update board
        #['X', '2', '3', '4', '5', '6', '7', '8', '9']
        board[move] = current_player

        #check if the curent payer has won
        if check_winner(board, current_player):
            clear_screen
            #redraw updated board
            print_board(board)
            print(f'Player {current_player} wins!')
            break

        # check if teh game is a draw
        if check_draw(board):
            clear_screen
            print_board(board)  
            print("It's a Draw!")
            break


        #switch player
        current_player = 'O' if current_player == 'X' else "X"



#play the game
play_tic_tac_toe()