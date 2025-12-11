import numpy as np


class GameOfLife:
    def __init__(self, start: np.ndarray):
        self._neighbors = np.zeros_like(start)
        self.state = start.copy()
        self._flop = np.zeros_like(self.state)

    def step(self) -> bool:
        self._neighbors.fill(0)

        self._neighbors += np.roll(self.state, -1, axis=0)  # bottom neighbors
        self._neighbors += np.roll(self.state, 1, axis=0)  # top neighbors
        self._neighbors += np.roll(self.state, -1, axis=1)  # right neighbors
        self._neighbors += np.roll(self.state, 1, axis=1)  # left neighbors

        self._neighbors += np.roll(
            self.state, (-1, -1), axis=(0, 1)
        )  # bottom right neighbors
        self._neighbors += np.roll(
            self.state, (-1, 1), axis=(0, 1)
        )  # bottom left neighbors
        self._neighbors += np.roll(
            self.state, (1, 1), axis=(0, 1)
        )  # top left  neighbors
        self._neighbors += np.roll(
            self.state, (1, -1), axis=(0, 1)
        )  # top right neighbors

        # each cell in `flop` now containes the number of neighbors at that site.
        # Conway's Game of Life rules are the following:
        # 1. Live cell with #neighbors < 2 dies
        # 2. Live cell with #neighbors == 2, 3 survives
        # 3. Live cell with #neighbors > 3 dies
        # 4. Dead cell with #neighbors == 3 comes to life

        alive = self.state > 0

        self._flop.fill(0)
        self._flop[(self._neighbors < 2) & alive] = 0
        self._flop[((self._neighbors == 2) | (self._neighbors == 3)) & alive] = 1
        self._flop[(self._neighbors > 3) & alive] = 0
        self._flop[(self._neighbors == 3) & ~alive] = 1

        self.state, self._flop = self._flop, self.state

        return self.state.sum().sum() != 0

    def simulate(self, max_iterations: int | None = None) -> None:
        if max_iterations is not None:
            for _ in range(max_iterations):
                if not self.step():
                    return
        else:
            while self.step():
                ...
