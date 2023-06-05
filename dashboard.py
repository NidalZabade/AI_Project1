import numpy as np

#The cave (the board) is a regular 8x8 chess board
number_of_rows = 8
number_of_columns = 8

#Initialize the cave (the board) with empty spaces (Initially its Empty)
Cave = np.full((number_of_rows, number_of_columns), ' ')

#Display the cave (the board)
def display_cave():
    #Print column labels
    column_labels = "   A   B   C   D   E   F   G   H"
    print(column_labels)

    #Print the row numbers in reversed order
    for row in reversed (range(number_of_rows)):
        #Print row number (end=' ' => to ensure that the next print statement continues on the same line)
        print(row + 1, end=' ')

        for column in range (number_of_columns):
            #Add the content of each cell in brackets
            print(f"[{Cave[row][column]}]", end=' ')
        #Print row number
        print(row + 1)
    #Print column labels again
    print(column_labels)
    
#Check for a win
def check_win(player):
    
    #Check horizontally if the player has 5 bricks in a row
    for row in range(number_of_rows):
        if np.count_nonzero(Cave[row] == player) >= 5:
            return True
    
    #Check vertically if the player has 5 bricks in a row
    for column in range(number_of_columns):
        if np.count_nonzero(Cave[:,column] == player) >= 5:
            return True
    
    #Check diagonally if the player has 5 bricks in a row (from left to right)
    for i in range(-4, 5):
        if np.count_nonzero(np.diagonal(Cave, i) == player) >= 5:
            return True
    
    #Check diagonally if the player has 5 bricks in a row (from right to left)
    for i in range(-4, 5):
        if np.count_nonzero(np.diagonal(np.fliplr(Cave), i) == player) >= 5:
            return True
    
    return False
def check_draw():
    #Check if all cells are occupied (full board)
    return np.count_nonzero(Cave == ' ') == 0

def is_valid_move(move):
    # a move is valid if it is a letter followed by a number
    if len(move) != 2:
        print("The move should be a letter followed by a number")
        return False
    
    column = move[0]
    row = move[1]
    
    
    # in the range A1-H8,
    if column < 'A' or column > 'H':
        print("The column should be in the range A-H")
        return False
    
    if row < '1' or row > '8':
        return False
    
    column = ord(column) - ord('A')
    row = int(row) - 1
    
    # the corresponding cell is empty 
    if Cave[row][column] != ' ':
        print("The cell is not empty")
        return False
    
    # if the column is A or H, then the brick can be placed anywhere in that column
    if column == 0 or column == 7:
        return True
    
    #has a brick on the left directly
    if column > 0 and Cave[row][column - 1] != ' ':
        return True
    
    #has a brick on the right directly
    if column < number_of_columns - 1 and Cave[row][column + 1] != ' ':
        return True
    
    print("The brick should be placed next to another brick")
    return False

def update_cave(move, player):
    #Update the cave (the board) with the move
    column = ord(move[0].upper()) - ord('A')
    row = int(move[1]) - 1
    Cave[row][column] = player


def enter_move(player):
    #Ask the player to enter a move
    move = input(f"Player {player}, enter your move: ")

    #Check if the move is valid
    while not is_valid_move(move):
        #Ask the player to enter a valid move
        move = input(f"Player {player}, enter a valid move: ")

    #Update the cave (the board) with the move
    update_cave(move, player)
