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
        #Print row number (end=' ' => to ensure that the next print statment co
        print(row + 1, end=' ')

        for column in range (number_of_columns):
            #Add the content of each cell in brackets
            print(f"[{Cave[row][column]}]", end=' ')
        #Print row number
        print(row + 1)
    #Print column labels again
    print(column_labels)

display_cave()