import numpy as np

# The cave (the board) is a regular 8x8 chess board
number_of_rows = 8
number_of_columns = 8


# Display the cave (the board)
def display_cave(board):
    # Print column labels
    column_labels = "   A   B   C   D   E   F   G   H"
    print(column_labels)

    # Print the row numbers in reversed order
    for row in reversed(range(number_of_rows)):
        # Print row number (end=' ' => to ensure that the next print statement continues on the same line)
        print(row + 1, end=" ")

        for column in range(number_of_columns):
            # Add the content of each cell in brackets
            print(f"[{board[row][column]}]", end=" ")
        # Print row number
        print(row + 1)
    # Print column labels again
    print(column_labels)


def check_win(player, board):
    # Check horizontally if the player has 5 bricks in a row .e.g. "WWWWW" not "WWWW  W"
    for row in range(number_of_rows):
        row_string = "".join(board[row, :])
        if player * 5 in row_string:
            return True

    # Check vertically if the player has 5 bricks in a row
    for column in range(number_of_columns):
        column_string = "".join(board[:, column])
        if player * 5 in column_string:
            return True

    # Check diagonally if the player has 5 bricks in a row (from left to right)
    for diagonal in range(-4, 5):
        diagonal_string = "".join(board.diagonal(diagonal))
        if player * 5 in diagonal_string:
            return True

    # Check diagonally if the player has 5 bricks in a row (from right to left)
    for diagonal in range(-4, 5):
        diagonal_string = "".join(np.fliplr(board).diagonal(diagonal))
        if player * 5 in diagonal_string:
            return True

    return False


def check_draw(board):
    # Check if all cells are occupied (full board)
    return np.count_nonzero(board == " ") == 0


def is_valid_move(move, board):
    # a move is valid if it is a letter followed by a number
    if len(move) != 2:
        return False, "The move should be a letter followed by a number"

    column = move[0]
    row = move[1]

    # in the range A1-H8,
    if column < "A" or column > "H":
        return False, "The column should be in the range A-H"

    if row < "1" or row > "8":
        return False, "The row should be in the range 1-8"

    column = ord(column) - ord("A")
    row = int(row) - 1

    # the corresponding cell is empty
    if board[row][column] != " ":
        return False, "The corresponding cell is not empty"

    # if the column is A or H, then the brick can be placed anywhere in that column
    if column == 0 or column == 7:
        return True, "The brick can be placed anywhere in that column"

    # has a brick on the left directly
    if column > 0 and board[row][column - 1] != " ":
        return True, "The brick should be placed next to another brick"

    # has a brick on the right directly
    if column < number_of_columns - 1 and board[row][column + 1] != " ":
        return True, "The brick should be placed next to another brick"

    return False, "The brick should be placed next to another brick"


def update_cave(move, board, player):
    # Update the cave (the board) with the move
    print(f"Player {player} moves to {move}")
    column = ord(move[0].upper()) - ord("A")
    row = int(move[1]) - 1
    board[row][column] = player
    return board


# Get all possible valid moves for the current board
def get_possible_valid_moves(board):
    possible_valid_moves = []

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            # Check if the cell is empty
            if board[row][column] == " ":
                # Check if the cell is valid
                valid_move, message = is_valid_move(
                    chr(column + ord("A")) + str(row + 1), board
                )
                if valid_move:
                    # Add the cell to the list of possible valid moves
                    possible_valid_moves.append(chr(column + ord("A")) + str(row + 1))

    return possible_valid_moves


def get_max_consecutive_bricks(board, player):
    max_consecutive_bricks = 0
    current_consecutive_bricks = 0

    for i in range(len(board)):
        if board[i] == player:
            current_consecutive_bricks += 1
        else:
            max_consecutive_bricks = max(
                max_consecutive_bricks, current_consecutive_bricks
            )
            current_consecutive_bricks = 0

    max_consecutive_bricks = max(max_consecutive_bricks, current_consecutive_bricks)

    return max_consecutive_bricks


def enter_move(board, player):
    # Ask the player to enter a move
    move = input(f"Player {player}, enter your move: ")

    valid_move, message = is_valid_move(move, board)

    # Keep asking the player to enter a move until the move is valid
    while not valid_move:
        print(message)
        move = input(f"Player {player}, enter your move: ")
        valid_move, message = is_valid_move(move, board)

    # Update the cave (the board) with the move
    board = update_cave(move, board, player)
    display_cave(board)
    return board
