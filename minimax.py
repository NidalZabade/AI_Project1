from dashboard import (
    check_win,
    check_draw,
    get_possible_valid_moves,
    get_max_consecutive_bricks,
    display_cave,
)
import numpy as np
from tree import Node


def heuristic(board, ai_player_symbol, human_player_symbol):
    # Heuristic function to evaluate the board and return a score; the score indicates how good the board is for the computer

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
        board_score += get_max_consecutive_bricks(board, ai_player_symbol) * 10
        # Check the maximum number of consecutive bricks for the human
        board_score -= get_max_consecutive_bricks(board, human_player_symbol) * 10
    return board_score


def generate_tree(root, player_symbol, depth):
    # Generate the tree of possible moves
    if depth == 0:
        return
    else:
        possible_moves = get_possible_valid_moves(root.get_board())
        for move in possible_moves:
            new_board = np.copy(root.get_board())
            row, column = int(move[1]) - 1, ord(move[0].upper()) - ord("A")
            new_board[row][column] = player_symbol
            new_node = Node(new_board)
            new_node.last_move = move  # Store the last move as an attribute of the Node
            root.add_child(new_node)
            generate_tree(new_node, "B" if player_symbol == "W" else "W", depth - 1)


def find_best_move(node, depth, maximizing_player, minimizing_player):
    # Implement the minimax algorithm to find the best move
    best_score = float('-inf')
    best_move = None
    for child in node.get_children():
        score = minimax(child, depth - 1, False, maximizing_player, minimizing_player)
        if score > best_score:
            best_score = score
            best_move = child.last_move  # Access the last move stored in the Node's attribute
    return best_move


def minimax(node, depth, is_maximizing, maximizing_player, minimizing_player):
    if depth == 0 or check_win(maximizing_player, node.get_board()) or check_win(minimizing_player, node.get_board()) or check_draw(node.get_board()):
        return heuristic(node.get_board(), maximizing_player, minimizing_player)

    if is_maximizing:
        best_score = float('-inf')
        for child in node.get_children():
            score = minimax(child, depth - 1, False, maximizing_player, minimizing_player)
            best_score = max(best_score, score)
            if best_score == 100:  # Immediate win
                break
        return best_score
    else:
        best_score = float('inf')
        for child in node.get_children():
            score = minimax(child, depth - 1, True, maximizing_player, minimizing_player)
            best_score = min(best_score, score)
            if best_score == -100:  # Immediate loss
                break
        return best_score


board = np.array([
    ["B", "B", "B", "B", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "W", " ", " ", " ", " "],
    ["B", "W", "W", " ", " ", " ", " ", " "],
    ["B", "W", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " "]
])

tree_depth = 3
root = Node(board)
generate_tree(root, "W", tree_depth)
best_move = find_best_move(root, tree_depth, "W", "B")

display_cave(root.get_board())
print("Best move:", best_move)
