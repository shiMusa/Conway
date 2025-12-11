import numpy as np
from numpy.testing import assert_array_equal
from src.conway.core import GameOfLife


def check_all_shifts(
    start: np.ndarray, expected: np.ndarray, simulation_steps: int
) -> None:
    for r in range(start.shape[0]):
        for c in range(start.shape[1]):
            s = np.roll(start, (r, c), axis=(0, 1))
            game = GameOfLife(s)
            game.simulate(simulation_steps)
            assert_array_equal(game.state, np.roll(expected, (r, c), axis=(0, 1)))
