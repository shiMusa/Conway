import numpy as np


def game_to_string(data: np.ndarray) -> str:
    (rows, cols) = data.shape

    symbols = [" ", "▀", "▄", "█"]
    game_str = "┌" + cols * "─" + "┐\n"

    for r in range(rows // 2):
        game_str += "│"
        for c in range(cols):
            index = int(data[r * 2, c] + 2 * data[r * 2 + 1, c])
            game_str += symbols[index]
        game_str += "│\n"

    if rows % 2 == 1:
        game_str += "│"
        for c in range(cols):
            index = int(data[-1, c])
            game_str += symbols[index]
        game_str += "│\n"

    game_str += "└" + cols * "─" + "┘\n"
    return game_str


def print_game(data: np.ndarray):
    print(game_to_string(data))
