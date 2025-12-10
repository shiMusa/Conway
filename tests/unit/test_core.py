import numpy as np
import itertools

from conway.core import simulation_step


# check the death of a cell at all possible positions in a 4x4 grid
def test_simulation_step_death():
    for r, c in itertools.product(range(4), repeat=2):
        start = np.zeros((4, 4))
        stop = np.zeros_like(start)
        start[r, c] = 1
        simulation_step(start, stop)
        stop == np.zeros((4, 4))
