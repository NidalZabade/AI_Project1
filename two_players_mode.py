from dashboard import display_cave, Cave, is_valid_move, check_win, check_draw


# manual entry for both ■’s moves and □’s moves
def manual_entry_for_both():
    # □ starts, followed by ■, then □ again,then ■ again, ...
    current_player = '□'
    while True:
        # Display the board
        display_cave()
        # Get the player's move
        move = input(f"Player {current_player} turn, enter your move (e.g., A1): ")
        # Convert the column letter to a numerical index for the board, (column A corresponds to index 0, column B  to index 1 and so on)
        column = ord(move[0].upper()) - ord('A')
        # Convert the row char to a numerical index for the board, (row #1 corresponds to index 0, row #2  to index 1 and so on)
        row = int(move[1]) - 1

        # Check if the move is valid
        if is_valid_move(move):
            # Place the brick in the chosen cell
            Cave[row][column] = current_player
            # Check if the current player has won
            if check_win(current_player):
                display_cave()
                print(f"Player {current_player} wins!")
                break

            # Switch to the next Player
            if current_player == '□':
                current_player = '■'

            else:
                current_player = '□'

        else:
            print("Invalid move :(, try again!")

        # Check if the board is full
        if check_draw():
            print("The game ends in a tie!")
            break
        