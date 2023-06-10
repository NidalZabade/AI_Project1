from dashboard import display_cave, Cave, is_valid_move, check_win, check_draw, get_possible_valid_moves
from minimax import find_best_move, generate_tree, Node
import numpy as np
# Manual entry for both B’s moves and W’s moves
def manual_entry_for_both():
    # W starts, followed by B, then W again, then B again, ...
    current_player = 'W'
    while True:
        # Display the board and all the possible moves
        display_cave(Cave)
        print("Possible moves: ", get_possible_valid_moves(Cave))

        # Get the player's move
        move = input(f"Player {current_player} turn, enter your move (e.g., A1): ")
        # Convert the column letter to a numerical index for the board (column A corresponds to index 0, column B corresponds to index 1, and so on)
        column = ord(move[0].upper()) - ord('A')
        # Convert the row char to a numerical index for the board (row #1 corresponds to index 0, row #2 corresponds to index 1, and so on)
        row = int(move[1]) - 1

        # Check if the move is valid
        if move in get_possible_valid_moves(Cave):
            # Place the brick in the chosen cell
            Cave[row][column] = current_player
            # Check if the current player has won
            if check_win(current_player, Cave):
                display_cave(Cave)
                print(f"Player {current_player} wins!")
                break

            # Switch to the next player
            if current_player == 'B':
                current_player = 'W'
            else:
                current_player = 'B'
        else:
            print("Invalid move :(, try again!")

        # Check if the board is full
        if check_draw(Cave):
            print("The game ends in a tie!")
            break

def W_manual_B_automatic( ):
    # W starts, followed by B, then W again, then B again, ...
    human = 'W'
    AI = 'B'
    current_player = human
    while True:
        if (current_player == human):
            # Display the board and all the possible moves
            display_cave(Cave)
            print("Possible moves: ", get_possible_valid_moves(Cave))

            # Get the player's move
            move = input(f"Player {current_player} turn, enter your move (e.g., A1): ")
            # Convert the column letter to a numerical index for the board (column A corresponds to index 0, column B corresponds to index 1, and so on)
            column = ord(move[0].upper()) - ord('A')
            # Convert the row char to a numerical index for the board (row #1 corresponds to index 0, row #2 corresponds to index 1, and so on)
            row = int(move[1]) - 1

            # Check if the move is valid
            if move in get_possible_valid_moves(Cave):
                # Place the brick in the chosen cell
                Cave[row][column] = current_player
                # Check if the current player has won
                if check_win(current_player, Cave):
                    display_cave(Cave)
                    print(f"Player {current_player} wins!")
                    break

                # Switch to the next player
                current_player = AI

            else:
                print("Invalid move :(, try again!")

            # Check if the board is full
            if check_draw(Cave):
                print("The game ends in a tie!")
                break 
        else:
                root = Node(Cave)
                generate_tree(root, "B", 3)
                display_cave(root.get_board())
                best_move = find_best_move(root, 3, True, "B", "W")
                # Convert the column letter to a numerical index for the board (column A corresponds to index 0, column B corresponds to index 1, and so on)
                column = ord(best_move[0].upper()) - ord('A')
                # Convert the row char to a numerical index for the board (row #1 corresponds to index 0, row #2 corresponds to index 1, and so on)
                row = int(best_move[1]) - 1
                # Place the brick in the chosen cell
                Cave[row][column] = current_player                
                print("AI move is:", best_move)
                  
                # Check if the current player has won
                if check_win(current_player, Cave):
                    display_cave(Cave)
                    print(f"AI wins!")
                    break

                # Check if the board is full
                if check_draw(Cave):
                    print("The game ends in a tie!")
                    break 
                
                # Switch to the next player
                current_player == human

def choose_game_mode():
    while True:
        print("\n*** Game Menu ***")
        print("1. Manual Entry for Both Players")
        print("2. Manual Entry with Computer (Player-W vs. AI-B)")
        print("3. Manual Entry with Computer (AI-B vs. Player-W)")
        print("4. Quit")
        choice = input("Select a game mode (1-4): ")

        if choice == '1':
            manual_entry_for_both()
        elif choice == '2':
            W_manual_B_automatic()  # Player is White (W), Computer is Black (B)
        elif choice == '3':
            B_manual_W_automaticr()  # Player is Black (B), Computer is White (W)
        elif choice == '4':
            print("Quitting the game...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    choose_game_mode()
