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

display_cave()

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
    #Check if all cells are occupied and no win condition is met
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if Cave[row][column] == ' ':
                return False
    return True

