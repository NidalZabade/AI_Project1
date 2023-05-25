#The cave (the board) is a regular 8x8 chess board
number_of_rows = 8
number_of_columns = 8

#Initialize the cave (the board) with empty spaces (Initially its Empty)
Cave = []

for row_num in range (number_of_rows):
    row = []

    for column_num in range(number_of_columns):
        cell = ' ' #Empty cell
        row.append(cell) #Add the cell to the current row

    Cave.append(row) #Add the row to the cave (the board)

#Display the cave (the board)
def display_cave():
    #Print column labels
    column_labels = "   A   B   C   D   E   F   G   H"
    print(column_labels)

    #Print the row numbers in reversed order (just
    for row in reversed (range(number_of_rows)):
        #Print row number (end=' ' => to ensure that the next print statment continues on the same line)
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
   #Check rows
   for row in range(number_of_rows):
       for column in range(number_of_columns - 4):
           #Check if there are 5 consecutive bricks for the same player in a row
           if all(Cave[row][column + i] == player for i in range (5)):
              return True

   #Check columns
   for column in range(number_of_columns):
       for row in range(number_of_rows - 4):
           #Check if there are 5 consecutive bricks for the same player in a column
           if all(Cave[row + i][column] == player for i in range (5)):
              return True

   #Check top-left to bottom-right diagonal
   for row in range(number_of_rows - 4):
       for column in range(number_of_columns - 4):
           #Check if there are 5 consecutive bricks for the same player in a top-left to bottom-right diagonal
           if all(Cave[row + i][column + i] == player for i in range (5)):
              return True

   # Check top-right to bottom-left diagonal
   for row in range(number_of_rows - 4):
       for column in range(4, number_of_columns):
       #Check if there are 5 consecutive bricks for the same player in a top-left to bottom-right diagonal
           if all(Cave[row][column - i] == player for i in range (5)):
              return True

   #No win condition found
   return False

def check_draw():
    #Check if all cells are occupied
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if Cave[row][column] == ' ':
                return False
    return True

def is_valid_move(move):
    # a move is valid if it is a letter followed by a number
    if len(move) != 2:
        print("The move should be a letter followed by a number (e.g. A1)")
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
    column = move[0]
    row = move[1]

    column = ord(column) - ord('A')
    row = int(row) - 1

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

def play_game():
    while True:
        display_cave()
        enter_move('X')
        
        
play_game()