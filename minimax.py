from dashboard import (
    check_win,
    check_draw,
    get_possible_valid_moves,
    display_cave,
)
from tree import Node
import numpy as np

number_of_rows = 8
number_of_columns = 8


def generate_tree(node, player_symbol, depth):
    if depth == 0:
        return
    else:
        possible_moves = get_possible_valid_moves(node.get_board())
        for move in possible_moves:
            new_board = np.copy(node.get_board())
            row, column = int(move[1]) - 1, ord(move[0].upper()) - ord("A")
            new_board[row][column] = player_symbol
            new_node = Node(new_board)
            new_node.last_move = move
            node.add_child(new_node)
            generate_tree(new_node, "B" if player_symbol == "W" else "W", depth - 1)


def minimax(node, depth, is_maximizing_player, maximizing_player, minimizing_player):
    if depth == 0 or check_win(maximizing_player, node.get_board()) or check_win(minimizing_player, node.get_board()) or check_draw(node.get_board()):
        maximizing_player_wins = check_win(maximizing_player, node.get_board())
        minimizing_player_wins = check_win(minimizing_player, node.get_board())
        is_draw = check_draw(node.get_board())
        
        
        #if maximizing_player_wins and minimizing_player_wins:
            #return 0, 0  # Game is a draw
            
            
        if maximizing_player_wins:
            return float("inf"), 0  # Max player wins
        if minimizing_player_wins:
            return float("-inf"), 0  # Min player wins
        if is_draw:
            return 0, 0  # Game is a draw
        return heuristic(node.get_board(), maximizing_player), 0  # Evaluation score

    if is_maximizing_player:
        best_score = float("-inf")
        best_move_count = 0
        for child in node.children:
            score, move_count = minimax(child, depth - 1, False, maximizing_player, minimizing_player)
            best_score = max(score, best_score)
            if score == best_score:
                best_move_count += move_count
        return best_score, best_move_count
    else:
        best_score = float("inf")
        best_move_count = 0
        for child in node.children:
            score, move_count = minimax(child, depth - 1, True, maximizing_player, minimizing_player)
            best_score = min(score, best_score)
            if score == best_score:
                best_move_count += move_count
        return best_score, best_move_count


def heuristic(board, player):
    player_score = 0
    opponent_score = 0

    # Check horizontally for consecutive bricks
    for row in range(number_of_rows):
        for column in range(number_of_columns - 4 + 1):
            window = list(board[row, column:column + 5])
            if window.count(player) == 5:
                return float("inf")  # Return maximum score if the player wins
            elif window.count(player) == 0 and window.count(" ") == 5:
                opponent_score += 1
            elif window.count(player) == 4 and window.count(" ") == 1:
                if column > 0 and board[row, column - 1] == " " and column + 5 < number_of_columns and board[
                    row, column + 5] == " ":
                    opponent_score += 1

    # Check vertically for consecutive bricks
    for column in range(number_of_columns):
        for row in range(number_of_rows - 4 + 1):
            window = list(board[row:row + 5, column])
            if window.count(player) == 5:
                return float("inf")  # Return maximum score if the player wins
            elif window.count(player) == 0 and window.count(" ") == 5:
                opponent_score += 1
            elif window.count(player) == 4 and window.count(" ") == 1:
                if row > 0 and board[row - 1, column] == " " and row + 5 < number_of_rows and board[
                    row + 5, column] == " ":
                    opponent_score += 1

    # Check diagonally from top-left to bottom-right
    for row in range(number_of_rows - 4 + 1):
        for column in range(number_of_columns - 4 + 1):
            window = list(board[row:row + 5, column:column + 5].diagonal())
            if window.count(player) == 5:
                return float("inf")  # Return maximum score if the player wins
            elif window.count(player) == 0 and window.count(" ") == 5:
                opponent_score += 1
            elif window.count(player) == 4 and window.count(" ") == 1:
                if row > 0 and column > 0 and board[row - 1, column - 1] == " " and row + 5 < number_of_rows and board[
                    row + 5, column + 5] == " ":
                    opponent_score += 1

    return opponent_score  # Return the opponent's score if no winning move found


def find_best_move(root, depth, is_maximizing_player, maximizing_player, minimizing_player):
    best_score, best_move_count = minimax(root, depth, is_maximizing_player, maximizing_player, minimizing_player)
    best_move = None
    for child in root.children:
        score, move_count = minimax(child, depth - 1, False, maximizing_player, minimizing_player)
        if score == best_score and move_count == best_move_count:
            best_move = child.last_move
            break
    return best_move


if __name__ == "__main__":
    board = np.array(
        [
            ["W", "W", "W", " ", " ", " ", " ", " "],
            ["B", "W", " ", " ", " ", " ", " ", " "],
            ["B", "W", "W", " ", " ", " ", " ", " "],
            ["B", " ", "B", " ", " ", " ", " ", " "],
            ["B", " ", "W", "B", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["B", "B", "B", " ", " ", " ", " ", " "],
        ]
    )
    root = Node(board)
    generate_tree(root, "W", 3)
    display_cave(root.get_board())
    best_move = find_best_move(root, 3, True, "W", "B")
    print("Best move:", best_move)