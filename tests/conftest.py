import numpy as np
from numpy.testing import assert_array_equal
from src.conway.core import simulation_step


def check_all_shifts(
    start: np.ndarray, expected: np.ndarray, simulation_steps: int
) -> None:
    for r in range(start.shape[0]):
        for c in range(start.shape[1]):
            s = np.roll(start, (r, c), axis=(0, 1))
            res = np.zeros_like(s)
            for _ in range(simulation_steps):
                simulation_step(s, res)
                s, res = res, s
            assert_array_equal(s, np.roll(expected, (r, c), axis=(0, 1)))
