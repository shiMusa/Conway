from typing import Generator
import numpy as np


def simulation_step(flip: np.ndarray, flop: np.ndarray) -> None:
    neighbors = np.zeros_like(flip)

    neighbors += np.roll(flip, -1, axis=0)  # bottom neighbors
    neighbors += np.roll(flip, 1, axis=0)  # top neighbors
    neighbors += np.roll(flip, -1, axis=1)  # right neighbors
    neighbors += np.roll(flip, 1, axis=1)  # left neighbors

    neighbors += np.roll(flip, (-1, -1), axis=(0, 1))  # bottom right neighbors
    neighbors += np.roll(flip, (-1, 1), axis=(0, 1))  # bottom left neighbors
    neighbors += np.roll(flip, (1, 1), axis=(0, 1))  # top left  neighbors
    neighbors += np.roll(flip, (1, -1), axis=(0, 1))  # top right neighbors

    # each cell in `flop` now containes the number of neighbors at that site.
    # Conway's Game of Life rules are the following:
    # 1. Live cell with #neighbors < 2 dies
    # 2. Live cell with #neighbors == 2, 3 survives
    # 3. Live cell with #neighbors > 3 dies
    # 4. Dead cell with #neighbors == 3 comes to life

    flop.fill(0)
    flop[(neighbors < 2) & (flip > 0)] = 0
    flop[((neighbors == 2) | (neighbors == 3)) & (flip > 0)] = 1
    flop[(neighbors > 3) & (flip > 0)] = 0
    flop[(neighbors == 3) & (flip == 0)] = 1


def simulate(
    initial_state: np.ndarray, max_iterations: int = 100
) -> Generator[np.ndarray, None, None]:
    flip = initial_state
    flop = np.zeros_like(initial_state)

    for _ in range(max_iterations):
        simulation_step(flip, flop)
        flip = flop
        yield flip
        if flip.sum().sum() == 0:
            break
