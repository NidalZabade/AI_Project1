from dashboard import (
    display_cave,
    update_cave,
    check_win,
    check_draw,
    get_possible_valid_moves,
    enter_move,
    number_of_rows,
    number_of_columns,
)
from minimax import AI_move
import numpy as np
import random


def two_players_mode():
    Cave = np.full((number_of_rows, number_of_columns), " ")
    turn = "B"
    while True:
        display_cave(Cave)
        Cave = enter_move(Cave, turn)

        if check_win(turn, Cave):
            display_cave(Cave)
            print(f"Player {turn} wins!")
            break

        if check_draw(Cave):
            display_cave(Cave)
            print("It's a draw!")
            break

        if turn == "B":
            turn = "W"
        else:
            turn = "B"


def player_vs_ai_mode(human_symbol, ai_symbol):
    Cave = np.full((number_of_rows, number_of_columns), " ")
    turn = "B"
    while True:
        display_cave(Cave)
        if turn == human_symbol:
            Cave = enter_move(Cave, turn)
        else:
            ai_move = AI_move(Cave, ai_symbol, 3)
            print(f"AI move: {ai_move}")
            Cave = update_cave(ai_move, Cave, ai_symbol)

        if check_win(turn, Cave):
            display_cave(Cave)
            print(f"Player {turn} wins!")
            break

        if check_draw(Cave):
            display_cave(Cave)
            print("It's a draw!")
            break

        if turn == human_symbol:
            turn = ai_symbol
        else:
            turn = human_symbol


if __name__ == "__main__":
    mode = input(
        "Choose mode\n1 for two players\n2 for player vs AI (AI starts)\n3 for player vs AI (player starts)\n4 for player vs AI (random)\n"
    )

    if mode == "1":
        two_players_mode()
    elif mode == "2":
        player_vs_ai_mode("W", "B")
    elif mode == "3":
        player_vs_ai_mode("B", "W")
    elif mode == "4":
        random.seed()
        if random.randint(0, 1) == 0:
            player_vs_ai_mode("W", "B")
        else:
            player_vs_ai_mode("B", "W")
    else:
        print("Invalid mode")
