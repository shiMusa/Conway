import argparse
from typing import Generator
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


def simulation_step(flip: np.ndarray, flop: np.ndarray):
    neighbors = np.zeros_like(flip)

    n_rows = flip.shape[0]
    n_cols = flip.shape[1]

    i_cols, i_rows = np.meshgrid(
        np.arange(0, n_cols),
        np.arange(0, n_rows),
    )

    i_right = (i_cols + 1) % n_cols
    i_left = (i_cols - 1) % n_cols
    i_top = (i_rows - 1) % n_rows
    i_bottom = (i_rows + 1) % n_rows

    neighbors += flip[i_bottom, i_cols]  # bottom neighbors
    neighbors += flip[i_top, i_cols]     # top    neighbors
    neighbors += flip[i_rows, i_right]   # right  neighbors
    neighbors += flip[i_rows, i_left]    # left   neighbors

    neighbors += flip[i_bottom, i_right]  # bottom right neighbors
    neighbors += flip[i_bottom, i_left]   # bottom left  neighbors
    neighbors += flip[i_top, i_left]      # top    left  neighbors
    neighbors += flip[i_top, i_right]     # top    right neighbors

    # each cell in `flop` now containes the number of neighbors at that site.
    # Conway's Game of Life rules are the following:
    # 1. Live cell with #neighbors < 2 dies
    # 2. Live cell with #neighbors == 2, 3 survives
    # 3. Live cell with #neighbors > 3 dies
    # 4. Dead cell with #neighbors == 3 comes to life

    flop[(neighbors < 2) & (flip > 0)] = 0
    flop[((neighbors == 2) | (neighbors == 3)) & (flip > 0)] = 1
    flop[(neighbors > 3) & (flip > 0)] = 0
    flop[(neighbors == 3) & (flip == 0)] = 1


def simulate(initial_state: np.ndarray, max_iterations: int = 100) -> Generator[np.ndarray, None, None]:
    flip = initial_state
    flop = np.zeros_like(initial_state)

    for _ in range(max_iterations):
        simulation_step(flip, flop)
        flip = flop
        yield flip
        if flip.sum().sum() == 0:
            break

def main():
    print("Hello from conway!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("")
    main()
