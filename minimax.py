from dashboard import (
    Cave,
    check_win,
    check_draw,
    get_possible_valid_moves,
    get_max_consecutive_bricks,
    display_cave,
)
import numpy as np
from tree import Node


def heuristic(board, ai_player_symbol, human_player_symbol):
    # Heuristic function to evaluate the board and return a score the score is how good the board is for the computer

    board_score = 0
    # Check if the computer wins
    if check_win(ai_player_symbol, board):
        board_score += 100
    # Check if the human wins
    elif check_win(human_player_symbol, board):
        board_score -= 100
    # Check if it is a draw
    elif check_draw(board):
        board_score += 50
    # Check the maximum number of consecutive bricks for the computer
    else:
        board_score += get_max_consecutive_bricks(board, ai_player_symbol)
        # Check the maximum number of consecutive bricks for the human
        board_score -= get_max_consecutive_bricks(board, human_player_symbol)
    return board_score


def generate_tree(root, player_symbol, depth):
    # Generate the tree of possible moves
    if depth == 0:
        return
    else:
        possible_moves = get_possible_valid_moves(root.get_board())
        # print(possible_moves)
        for move in possible_moves:
            new_board = np.copy(root.get_board())
            row, column = int(move[1]) - 1, ord(move[0].upper()) - ord("A")
            # print(row, column, move)
            new_board[row][column] = player_symbol
            # print in the test2.txt
            # file = open("test2.txt", "a")
            # file.write(
            #     str(
            #         heuristic(
            #             new_board,
            #             "W" if player_symbol == "W" else "B",
            #             "B" if player_symbol == "W" else "W",
            #         )
            #     )
            #     + "\n"
            # )
            # file.write(str("player: " + player_symbol + "\n"))

            # file.write(str(new_board))
            # file.write("\n")
            # file.close()
            new_node = Node(new_board)
            root.add_child(new_node)
            generate_tree(new_node, "B" if player_symbol == "W" else "W", depth - 1)


def print_tree_file(root):
    file = open("tree.txt", "a")
    file.write(str(root.get_board()))
    file.write("\n")
    for child in root.get_children():
        print_tree_file(child)
    file.close()


board = np.full((8, 8), " ")
board[0][0] = "W"
board[0][1] = "W"
board[0][2] = "W"
board[0][3] = "W"
board[7][0] = "B"
board[7][1] = "B"
board[7][2] = "B"
board[7][3] = "B"
display_cave(board)


tree_depth = 2

# Create the root node
root = Node(board)

file = open("test2.txt", "w")
file.write("")
file.close()
# Generate the tree
generate_tree(root, "W", tree_depth)

# Print the tree to text file


print("Tree generated")
# root.print_tree()

print("Best move:")
